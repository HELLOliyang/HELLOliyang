# 2.21练习
# 2-5
# a = 1
# while a <=10:
#     print(a)
#     a = a + 1
# for a in range(11):
#     print(a)
# 2-6
# a = int(input('请输入：'))
# if a>0:
#     print(str(a)+'是正数')
# elif a==0:
#     print(str(a)+'是0')
# else:
#     print(str(a)+'是负数')
#2-7
# a = str(input('请输入：'))
# b = 0
# while b < len(a):
#     print(a[b])
#     b = b+1
# for i in range(len(a)):
#     print(a[i])
# 2-8
# a = [1,3,2,4,6]
# b = 0
# c = 0
# while b < len(a):
#     c = a[b]+c
#     b = b+1
# print(c)
# for b in a:
#     c = b+c
# print(c)
# a = []
# b = 0
# c = 0
# while b < 5:
#     d = int(input('输入数字：'))
#     c = d +c
#     a.append(d)
#     b = b+1
# for b in range(0,5):
#     d = int(input('输入数字：'))
#     c = d +c
#     a.append(d)
# print(a)
# print(c)
#2-9
# a = [1,3,2,4,7,8]
# b = 0
# c = 0
# while b < len(a):
#     c = a[b]+c
#     b = b+1
# avg = c/len(a)
# print(avg)
# a = []
# d = 0
# for b in range(5):
#     c = float(input('请输入数字：'))
#     a.append(c)
#     d = d+c
# print(a)
# print(d/5)
# 2-10
# lottery=45
# status=1
# while status == 1:
#     num=float(input("Enter a num[1,100]:"))
#     if num > 100:
#         print("It's is large.")
#         print(status)
#     elif num < 1:
#         print("It's is litte.")
#         print(status)
#     else:
#         print("Congratulations!you got the num!")
#         print(status)
#         status=0
# print(status)
#2-11
# def nsum():
#     a = []
#     d = 0
#     for b in range(5):
#         c = float(input('请输入数字：'))
#         a.append(c)
#         d = d+c
#     print(d)
# def navg():
#     a = []
#     d = 0
#     for b in range(5):
#         c = float(input('请输入第'+str(b+1)+'个数字：'))
#         a.append(c)
#         d = d + c
#     print(d/5)
# print('1:求和，2求平均值，x关闭')
# select = input('输入选择：')
# if select == '1':
#     nsum()
# elif select == '2':
#     navg()
# elif select == 'X':
#     exit()
# else:
#     print('dsdds')
#2-12
# a = []
# for i in range(3):
#     c = int(input('输入:'))
#     a.append(c)
# print(a)
# for q in range(len(a)):
#     for p in range(q+1,len(a)):
#         if a[q] > a[p]:
#             a[q],a[p] = a[p],a[q]
# print(a)
# b = sorted(a,reverse=True)
# a.sort()


import os
#获取文件名称
# while True:
#     if os.path.exists('fname'):
#         print('重复')
#     else:
#         break
# all = []
# print('按.推出')
# while True:
#     entry = input('> ')
#     if entry == '.':
#         break
#     else:
#         all.append(entry)
# a = [str(x) for x in all]
# c = ''.join(a)
# try:
#     fobj = open(c,'w+')
#     fobj.write(c)
#     print(c)
#     # fobj.close()
#     print('done')
#     txt = fobj.read()
#     print(txt)
# except IOError as e:
#     print(e)
# print('perfect')
# print(abs(-23))
# def is_palindrome(n):
#    a = "".join(list(n))
#    L = []
#    # print(a)
#    for i in range(len(a)):
#         print(i)
#         q = a[i]
#         p = a[-i-1]
#         if q != p:
#             L.append('False')
#         else:
#             L.append('True')
#    print(L)
#
# out = list(filter(is_palindrome,['12321','9010109','134']))
# print(out)
def findMinAndMax(L):
    # L = [7, 1, 3, 9, 5]
    i = 0
    j = 0
    for j in range(len(L)-1):
        for i in range(len(L)-1):
            if L[i] > L[i+1]:
                L[i],L[i+1] = L[i+1],L[i]
    return(L)


# 测试
# if findMinAndMax([]) != (None, None):
#     print('测试失败!')
# if findMinAndMax([7]) != (7):
#     print('测试失败!')
# if findMinAndMax([7, 1]) != (1, 7):
#     print(L)
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 3, 5, 7, 9):
#     print('测试失败!')
# else:
#     print('测试成功!')
a = findMinAndMax([7, 1])
b =findMinAndMax([7, 1, 3, 9, 5])
print(a)
print(b)