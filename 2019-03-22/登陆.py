#!/usr/bin/python
# -*- coding: utf-8 -*-

# 作者: itdeer
# 时间: 2019/3/22

# _username = "sundafei"
# _password = "123"
#
# flag = False
#
# for i in range(3):
#
#     username = input("Username:")
#     password = input("Password:")
#
#     if username == _username and password == _password :
#         print("Welcome %s login..." % username)
#         flag = True
#         break
#     else:
#         print("Username or Password Invalid.....")
#
# if not flag:
#     print("连续输入三次错误")




# _username = "sundafei"
# _password = "123"
#
# flag = False
#
# for i in range(3):
#
#     username = input("Username:")
#     password = input("Password:")
#
#     if username == _username and password == _password :
#         print("Welcome %s login..." % username)
#         flag = True
#         break
#     else:
#         print("Username or Password Invalid.....")
# else:
#     print("连续输入三次错误")



_username = "sundafei"
_password = "123"

num = 0

while num < 3:
    username = input("Username:")
    password = input("Password:")

    if username == _username and password == _password :
        print("Welcome %s login..." % username)
        break
    else:
        print("Username or Password Invalid.....")

    num += 1
else:
    print("连续输入三次错误")