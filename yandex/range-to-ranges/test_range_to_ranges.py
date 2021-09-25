from typing import List


def dump_xrange(interval):
    if len(interval) > 1:
        return f"{interval[0]}-{interval[-1]}"
    elif len(interval) == 1:
        return f"{interval[0]}"
    else:
        return ""


def xrange(input_list: List[int]) -> str:
    sorted_list = sorted(input_list)
    intervals: List[str] = []

    prev = None
    interval = []
    for i in sorted_list:
        if prev is not None and (i - prev) != 1:
            intervals.append(dump_xrange(interval))
            interval = []

        prev = i
        interval.append(str(i))

    intervals.append(dump_xrange(interval))

    return ",".join(intervals)


def test_t1():
    input_list = [1, 2, 4, 5, 8, 9, 10, 0, 12]
    assert xrange(input_list) == "0-2,4-5,8-10,12"


def test_t2():
    input_list = [1, 2, 3, 4]
    assert xrange(input_list) == "1-4"


def test_t3():
    input_list = [1, 4]
    assert xrange(input_list) == "1,4"


def test_t4():
    input_list = [1, 3, 5]
    assert xrange(input_list) == "1,3,5"


def test_t5():
    input_list = [1, 3, 5, 6, 7]
    assert xrange(input_list) == "1,3,5-7"


def test_t6():
    input_list = [1, 3, 5, 0]
    assert xrange(input_list) == "0-1,3,5"


def test_t7():
    input_list = [1]
    assert xrange(input_list) == "1"


def test_t8():
    input_list = []
    assert xrange(input_list) == ""
