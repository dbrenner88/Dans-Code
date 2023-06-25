'''
print("hello world")

a = 3
b = 4

if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("i don't know what the world has come to")

mydict = {
    "a": 4,
    "b": 10,
    "c": 11
}
print(mydict["c"])

if mydict["a"] > mydict["c"]:
    print("i love lamp " + mydict["c"])
else: 
    print("gotcha")

while b < 15:
    b +=1
    print(b)

fruits = ["apple", "kiwi", "banana"]
for x in fruits:
    print(x + ": this fruit is " + str(len(x)) + " characters")
    if x == "kiwi":
        break
'''

nums1 = [1,2,3,0,0,0] 
m = 3 
nums2 = [2,5,6]
n = 3 

while n > 0:
    if m <= 0 or nums2[n-1] >= nums1[m-1]:  
        nums1[m+n-1] = nums2[n-1]
        n -= 1
    else:
        nums1[m+n-1] = nums1[m-1]
        m -= 1
## merged_array = sorted(nums1 + nums2 + [m] + [n])
'''for j in range(m):
    nums1[m+j] = nums2[j]
nums1 = sorted(nums1)
'''
##nums1 = sorted(nums1.extend(nums2))

print(nums1)




