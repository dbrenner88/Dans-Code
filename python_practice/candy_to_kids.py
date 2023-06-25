# class Solution:
#     def candy(self, ratings: list[int]) -> int:
#         n = len(ratings)
#         candies = [1] * n
#         for i in range(1, n):
#             if ratings[i] > ratings[i - 1]:
#                 candies[i] = candies[i - 1] + 1
#         for i in range(n - 2, -1, -1):
#             if ratings[i] > ratings[i + 1]:
#                 candies[i] = max(candies[i], candies[i + 1] + 1)
#         return candies, sum(candies)


# ratings = [1, 2, 2, 5, 6]
# rate = Solution()
# print(ratings)
# print(rate.candy(ratings))

# python code
# class DictMeta(type):
#     def __new__(mcs, name, bases, attrs, **kwargs):
#         new_attrs = {}
#         for key, value in attrs.items():
#             if isinstance(value, dict):
#                 new_attrs.update(value)
#             else:
#                 new_attrs[key] = value
#         return super().__new__(mcs, name, bases, new_attrs)


# class MyClass(metaclass=DictMeta):
#     def __init__(self, name = None, age=None):
#         self.name = name
#         self.age = age


# my_instance = MyClass('Alice', 28)
# print(my_instance.name, my_instance.age)

# danielbrenner@daniels-mbp python_practice % python3 candy_to_kids.py
# {'name': 'Alice', 'age': 28} None

# def primes(limit):
#     i = 2
#     while i < limit:
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             yield i
#         i += 1


# print(list(primes(50)))
with open('output.txt', 'w') as f:
    f.write('hello, world\n')
