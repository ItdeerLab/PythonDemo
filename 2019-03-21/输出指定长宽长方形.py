#!/usr/bin/python
# -*- coding: utf-8 -*-

# 作者: itdeer
# 时间: 2019/3/21


## 输出指定长宽的长方形


flag = True
while flag :
    lon = int(input("请输入长:"))
    wid = int(input("请输入宽:"))
    if lon <= 0 or wid <= 0:
        print("输入的长度和宽度不能小于0，请重新输入...")
    else:
        flag = False


while wid > 0:
    tmp=lon
    while tmp > 0:
        print("*",end="")
        tmp -= 1
    wid -= 1
    print()