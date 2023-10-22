"""
https://py.checkio.org/en/mission/duplicate-zeros/

You are given list of integers (int).
Your task in this mission is to duplicate all zeros and return the result as any Iterable.

Let's look on the example:
[1, 0, 2, 0] -> [1, 0, 0, 2, 0, 0]
"""

from collections.abc import Iterable


# simple solution
def duplicate_values(donuts: list[int], value=0) -> Iterable[int]:
    result = []
    for i in donuts:
        result.append(i)
        if i == value:
            result.append(value)
    return result


if __name__ == '__main__':
    print("__RUN_TESTS__:")

    test_1 = [1, 0, 2, 3, 0, 4, 5, 0]
    print(test_1, ' -->> ', list(duplicate_values(test_1)))

    # These "asserts" are used for self-checking
    assert list(duplicate_values([1, 0, 2, 3, 0, 4, 5, 0])) == [1, 0, 0, 2, 3, 0, 0, 4, 5, 0, 0]
    assert list(duplicate_values([0, 0, 0, 0])) == [0, 0, 0, 0, 0, 0, 0, 0]
    assert list(duplicate_values([100, 10, 0, 101, 1000])) == [100, 10, 0, 0, 101, 1000]

    print('DONE - OK')
