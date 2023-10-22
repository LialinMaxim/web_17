"""
https://py.checkio.org/en/mission/duplicate-zeros/

You are given list of integers (int).
Your task in this mission is to duplicate all zeros and return the result as any Iterable.

Let's look on the example:
[1, 0, 2, 0] -> [1, 0, 0, 2, 0, 0]
"""

import re
from collections.abc import Iterable


# more complex
# def duplicate_zeros(donuts: list) -> list:
#     print('# juniors do: ', donuts)
#     a = [x for x, y in enumerate(donuts) if y == 0]
#
#     for i, j in enumerate(a):
#         print(i, j)
#         donuts.insert(i + j + 1, 0)
#     return donuts


# like trainee do
# def duplicate_zeros(num):
#     print('# like trainee do: ', num)
#     u = ["0"]
#     t = num[::-1]
#     y = ' '.join(map(str, t)).replace(" 0", " 0 0").split()[::-1]
#     if all(char in u for char in y):
#         y.append(0)
#         return list(map(int, y))
#
#     elif y[len(y) - 1] == "0":
#         y.append(0)
#         return list(map(int, y))
#
#     else:
#         return list(map(int, y))

## with extra unnecessary actions
# def duplicate_zeros(donuts: list) -> list:
#     print('# with extra unnecessary actions: ', donuts)
#     return list(map(int, (' ' + ' '.join(map(str, donuts))).replace(' 0', ' 0 0')[1:].split()))


## too difficult
def duplicate_zeros(donuts: list) -> list:
    print('# too difficult: ', donuts)
    return sum([[x] * ((x == 0) + 1) for x in donuts], [])

## much more difficult
# duplicate_zeros = lambda d: eval(re.sub(r"(?<!\d)(0)", r"\1, 0", str(d)))

## difficult to read
duplicate_zeros=f=lambda d:d and[d[0]]+[0]*(d[0]==0)+f(d[1:])


## difficult to read 2
# duplicate_zeros = lambda d: [y for x in d for y in ([x] if x else [x, x])]


if __name__ == '__main__':
    print("__RUN_TESTS__:")

    test_1 = [1, 0, 2, 3, 0, 4, 5, 0]
    print(test_1, ' -->> ', list(duplicate_zeros(test_1)))

    # These "asserts" are used for self-checking
    assert list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])) == [1, 0, 0, 2, 3, 0, 0, 4, 5, 0, 0]
    assert list(duplicate_zeros([0, 0, 0, 0])) == [0, 0, 0, 0, 0, 0, 0, 0]
    assert list(duplicate_zeros([100, 10, 0, 101, 1000])) == [100, 10, 0, 0, 101, 1000]

    print('DONE - OK')
