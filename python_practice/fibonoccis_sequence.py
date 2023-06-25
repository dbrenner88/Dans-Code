def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield b
        a, b = b, a+b


# print(list(fibonacci(10)))


def get_odd_numbers(nums):
    odd_nums = filter(lambda num: num % 2 == 1, nums)
    return odd_nums


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(get_odd_numbers(nums)))
