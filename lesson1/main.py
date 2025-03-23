import datetime


def run_time(function):
    def inner():
        time1 = datetime.datetime.now()
        function()
        time2 = datetime.datetime.now()
        print(time2 - time1)

    return inner


@run_time
def print_shalom():
    index = 0
    for _ in range(200):
        print(f"Shalom! You are number {index}")
        index = index + 1


print_shalom()

dict = {}


def cache(func):
    def inner(num):
        if dict.keys().__contains__(num):
            dict[num]
        else:
            result = func(num)
            dict[num] = result
            return result

    return inner

@cache
def fibonachi(num):
    num1 = 0
    num2 = 1
    for _ in range(num - 1):
        num3 = num1 + num2
        num1 = num2
        num2 = num3
    return num2


def fib():
    for i in range(68):
        print(fibonachi(i))


fib()
