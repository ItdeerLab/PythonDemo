#!/usr/bin/python
# -*- coding: utf-8 -*-

# 作者: itdeer
# 时间: 2019/3/28


f = open("demo1", "r")

# print(f.read(7))
# print(f.readline(18))
# print(f.readlines())
# for i in f.readlines():
#     print(i.strip("\n"))
#
# f.close()


data = f.readlines()
f.close()


# for i in data:
#     print(i.strip())

# num = 0
# for i in data:
#     num += 1
#     if num == 6:
#         print(i.strip() + " tianjia nei rong")
#     else:
#         print(i.strip())


# num = 0
# for i in data:
#     num += 1
#     if num == 6:
#         i += i.strip() + " tianjia nei rong"
#     print(i.strip())


# num = 0
# for i in data:
#     num += 1
#     if num == 6:
#         i = "".join([i.strip(), " tianjia nei rong"])
#     print(i.strip())


data[5] = "".join([data[5].strip(), " tianjia nei rong"])
for i in data:
    print(i.strip())

