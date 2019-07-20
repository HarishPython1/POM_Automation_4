# # # # def my_function(a, b):
# # # #     c = a + b
# # # #     d = a - b
# # # #     return c, d
# # # #
# # # #
# # # # x, y = my_function(10, 20)
# # # # print(x)
# # # # print(y)
# # # #
# # # #
# # # # def my_fun(institute):
# # # #     c = "welcome to " + institute
# # # #     return c
# # # #
# # # # x=my_fun("Qspiders")
# # # # print(x)
# # # # x=my_fun("Jspiders")
# # # # print(x)
# # # #
# # # # def m():
# # # #     return (1,2,3,4)
# # # #
# # # # x=m()
# # # # print(x)
# # #
# # #
# # # a=200
# # # def f():
# # #     global a
# # #     print(a)
# # #     a=100
# # #     print(a)
# # #
# # # f()
# # # print(a)
# # #
# # # def f1(l):
# # #     print(l)
# # #
# # # f1([1,2,3,4])
# # #
# #
# # # a = [int(x) for x in input().split()]
# # # print(a)
# #
# #
# # def calculate(l):
# #     sum = 0
# #     n = len(l)
# #     for i in l:
# #         sum = sum + i
# #         avg = sum / n
# #         return sum, avg
# #
# #
# # def a():
# #     print("enter numbers")
# #     l = [int(x) for x in input().split()]
# #     for i in l:
# #         print(i)
# #         return 100
# #
# #
# # x = a()
# # print(x)
# #
# # # x, y = calculate(l)
# # # print(x)
# # # print(y)
#
# # def a():
# #     print(100)
# #     a()
# #
# # a()
#
#
# def factorial(n):
#     if n == 0:
#         res = 1
#     else:
#         res = n * factorial(n - 1)
#     return res
#
#
# # val=factorial(4)
# # print(val)
# for i in range(1, 11):
#     print("Facto of num {} is {} ".format(i, factorial(i)))

# f = lambda x, y: x + y
# a=f(2,3)
# print(a)

#
# max=lambda x,y:x if x>y else y
# a,b=[int(x) for x in input().split(',')]
# print(max(a,b))

l=[1,2,3,4]
print(len(l))
