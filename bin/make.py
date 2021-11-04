import logging
import pathlib
import re
from dataclasses import dataclass

import click
import jinja2
import requests

logging.basicConfig(
    level="INFO",
)
Template = jinja2.Template("""\"\"\"{{ task.title }}

Difficulty: {{ task.difficulty }} 
URL: {{ task.url }}
\"\"\"

{{ task.comment }}


class Solution:
    @staticmethod
    def {{ task.method.name }}({{ task.method.args }}){% if task.method.returning %} -> {{ task.method.returning }}{% endif %}:
        pass


def test_case_0():
    # TODO: Add params
    result = Solution.{{ task.method.name }}()
    assert result == ""

""")


@dataclass
class Method:
    name: str
    args: str
    returning: str


@dataclass
class Task:
    id: int
    url: str
    title: str
    slug: str
    difficulty: str
    snippet: str
    comment: str
    method: Method


def download_leetcode_task(name: str):
    url = f"https://leetcode.com/graphql"
    params = {
        "operationName": "questionData",
        "variables": {
            "titleSlug": name,
        },
        "query": "query questionData($titleSlug: String!) {\n"
                 "  question(titleSlug: $titleSlug) {\n"
                 "    questionFrontendId\n"
                 "    title\n"
                 "    titleSlug\n"
                 "    difficulty\n"
                 "    codeSnippets {\n"
                 "      langSlug\n"
                 "      code\n"
                 "    }\n"
                 "  }\n"
                 "}\n"
    }

    response = requests.post(url, json=params)
    return response.json()


def leetcode_parser(json: dict) -> Task:
    def camel_to_snake(name):
        name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

    def get_comment(snippet_data: str) -> str:
        comments = []
        for line in snippet_data.split("\n"):
            if line.startswith("# "):
                comments.append(line)
            else:
                break

        return "\n".join(comments)

    def get_method(snippet_data: str) -> Method:
        regexp = r"\n\s+def\s*([^(]+)\(self,\s*([^)]+)\)(\s*->\s*([^:]+))?:"
        result = re.search(regexp, snippet_data)

        return Method(
            name=camel_to_snake(result.groups()[0]),
            args=result.groups()[1],
            returning=result.groups()[-1],
        )

    task_data = json["data"]["question"]

    url = f"https://leetcode.com/problems/{task_data['titleSlug']}/"
    snippet = list(filter(lambda x: x["langSlug"] == "python3", task_data.pop("codeSnippets")))[0]

    return Task(
        id=task_data["questionFrontendId"],
        url=url,
        title=task_data["title"],
        slug=task_data["titleSlug"],
        difficulty=task_data["difficulty"],
        snippet=snippet["code"],
        comment=get_comment(snippet["code"]),
        method=get_method(snippet["code"]),
    )


def make_leetcode_template(project: str, name: str):
    json = download_leetcode_task(name)
    task = leetcode_parser(json)

    task_dir = f"{task.id}-{task.slug}"
    full_task_dir = f"{project}/{task_dir}"
    task_path = f"test_{task.id}_{task.slug.replace('-', '_')}.py"
    full_task_path = f"{full_task_dir}/{task_path}"
    pathlib.Path(f"{project}/{task_dir}").mkdir(parents=True, exist_ok=True)

    if pathlib.Path(full_task_path).exists():
        logging.error(f"File {full_task_path} already exists")
        return

    Template.stream(task=task).dump(full_task_path)
    logging.info(f"Write file {full_task_path}")


def make_hackerrank_template(project: str, name: str):
    pass


@click.command()
@click.argument('project',
                type=click.Choice(['leetcode'], case_sensitive=False))
@click.argument('name')
def make_template(project, name):
    """Simple program that greets NAME for a total of COUNT times."""
    project_map = {
        "leetcode": make_leetcode_template,
        "hackerrank": make_hackerrank_template,
    }
    pathlib.Path(project).mkdir(parents=True, exist_ok=True)
    project_func = project_map[project]
    project_func(project, name)


if __name__ == '__main__':
    make_template()
