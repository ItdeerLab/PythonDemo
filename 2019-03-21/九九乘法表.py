#!/usr/bin/python
# -*- coding: utf-8 -*-

# 作者: itdeer
# 时间: 2019/3/21

## 99 乘法表

# 1 * 1 = 1
# 1 * 2 = 2  2 * 2 = 4
# 1 * 3 = 3  2 * 3 = 6  3 * 3 = 9
# 1 * 4 = 4  2 * 4 = 8  3 * 4 = 12  4 * 4 = 16

num = 1
while num <= 9:
    tmp = 1
    while tmp <= num:
        print(str(tmp) + " * " + str(num) + " = " + str(tmp * num), end="  ")
        tmp += 1
    num +=1
    print()