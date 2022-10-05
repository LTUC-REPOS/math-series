import pytest

from series.series import fibo,lucas,sum_series


"""

Fibonacci:

The first 10 elements:

[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

n = 0 --> 0
n = 4 --> 2
n = 10 --> 34
n = -50 --> -1
n = "Hi" --> -1

"""


def test_fib_1():
    actual = fibo(0)
    expected = 0
    assert actual == expected

def test_fib_2():
    actual = fibo(4)
    expected = 2
    assert actual == expected

def test_fib_3():
    actual = fibo(10)
    expected = 34
    assert actual == expected

def test_fib_4():
    actual = fibo(-50)
    expected = -1
    assert actual == expected

def test_fib_5():
    actual = fibo("Hi")
    expected = -1
    assert actual == expected




"""

Lucas:

The first 10 elements:

[2, 1, 3, 4, 7, 11, 18, 29, 47, 76]

n = 0 --> 2
n = 4 --> 4
n = 10 --> 76
n = -5 --> -1
n = "Hello" --> -1

"""


def test_lucas_1():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_2():
    actual = lucas(4)
    expected = 4
    assert actual == expected

def test_lucas_3():
    actual = lucas(10)
    expected = 76
    assert actual == expected

def test_lucas_4():
    actual = lucas(-5)
    expected = -1
    assert actual == expected

def test_lucas_5():
    actual = lucas("Hello")
    expected = -1
    assert actual == expected



"""

Sum Series:

Formula:

[x, y, x+y, x+2y, 2x+3y, 3x+5y, 5x+8y .... ]

The first 10 elements (assuming x=2,y=2):

[2, 2, 4, 6, 10, 16, 26, 42, 68, 110]

n = 0 --> 2
n = 4 --> 10
n = 10 --> 110
n = -3 --> -1
n = "String" --> -1
x = "yes" and y= any --> -1
y = "str" and x = any --> -1
"""



def test_sum_series_1():
    actual = sum_series(0,2,2)
    expected = 2
    assert actual == expected

def test_sum_series_2():
    actual = sum_series(4,2,2)
    expected = 6
    assert actual == expected

def test_sum_series_3():
    actual = sum_series(10,2,2)
    expected = 110
    assert actual == expected

def test_sum_series_4():
    actual = sum_series(-3)
    expected = -1
    assert actual == expected

def test_sum_series_5():
    actual = sum_series("string")
    expected = -1
    assert actual == expected

def test_sum_series_6():
    actual = sum_series(10,"yes",2)
    expected = -1
    assert actual == expected

def test_sum_series_7():
    actual = sum_series(10,2,'yes')
    expected = -1
    assert actual == expected

