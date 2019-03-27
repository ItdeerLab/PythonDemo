#!/usr/bin/python
# -*- coding: utf-8 -*-

# 作者: itdeer
# 时间: 2019/3/21

## 判断输入的三个值的最大值

num1 = input("num1:")
num2 = input("num2:")
num3 = input("num3:")

if num2 > num1 :
    num1 = num2
if num3 > num1 :
    num1 = num3

print("最大值：" + num1)