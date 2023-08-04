
import random as r

fruits = ["Apple", "Peach", "Pear"]

for n in fruits:
    print(n)
    print(n + " pie")
print(fruits)

n = 0
rand_int = r.randint(1, 1000)

for n in range(0, rand_int):
    n += 1
print(n)

'''
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

sum_height = 0
cnt_heights = 0

for i in student_heights:
    sum_height += i
    cnt_heights += 1

print(round(sum_height/cnt_heights))
'''
sum_num = 0
for number in range(2, 101, 2):
    sum_num += number
    print(number)
print(sum_num)
