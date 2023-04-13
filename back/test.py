# data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
# def fun(m):
#     v = m[0][0]

#     for row in m:
#         for element in row:
#             if v < element: v = element

#     return v
# print(fun(data[0]))


# a=[1,2,3,4,5]
# print(a[3:0:-1])

# arr = [1, 2, 3, 4, 5, 6]
# for i in range(1, 6):
#     arr[i - 1] = arr[i]
# for i in range(0, 6):
#     print(arr[i], end = " ")

# def f(value, values):
#     v = 1
#     values[0] = 44
# t = 3
# v = [1, 2, 3]
# f(t, v)
# print(t, v[0])

# a=[1,2,3,4,5,6,7,8,9]
# print(a[::2])

# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60
# print(a)


# #Find missing number
# array_nums = [1,2,3,4,6]
# def mis_num(array_nums):
#     sum1 = 6*7/2
#     sum2 = sum(array_nums)
#     print(sum1 - sum2)

# mis_num(array_nums)


# array_nums = [3,6,7,10,11]

# def find_pairs(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] == nums[j]:
#                 continue
#             elif nums[i] + nums[j] = target:
#                 print(i, j)
