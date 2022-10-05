


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

def fibo(n):

    if type(n) != int or n < 0:
        return -1

    starting = [0,1]

    if n < 2:
        return starting[n]

    for val in range(n-2):
            sum = starting[val] + starting[val+1]             
            starting.append(sum)
    print(starting)
    print(starting[n-1])
    return starting[n-1]

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

def lucas(n):

    if type(n) != int or n < 0:
        return -1

    starting = [2,1]


    if n < 2:
        return starting[n]

    for val in range(n-2):
            sum = starting[val] + starting[val+1]             
            starting.append(sum)
    print(starting)
    print(starting[n-1])
    return starting[n-1]

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

def sum_series(n,x=0,y=1):

    if type(n) != int or n < 0:
        return -1
    if type(x) != int or x < 0:
        return -1
    if type(y) != int or y < 0:
        return -1

    starting = [x,y]

    if n < 2:
        return starting[n]

    for val in range(n-2):
            sum = starting[val] + starting[val+1]             
            starting.append(sum)
    print(starting)
    print(starting[n-1])
    return starting[n-1]



