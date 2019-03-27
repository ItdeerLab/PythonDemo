#!/usr/bin/python
# -*- coding: utf-8 -*-

# 作者: itdeer
# 时间: 2019/3/21

## 输出以下图形


# *
# * *
# * * *
# * * * *
# * * * * *

col=1
row=1

while row <= 5 :
    tmp = col
    while tmp <= row:
        print("*", end="")
        tmp += 1
    row += 1
    print()