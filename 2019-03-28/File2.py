#!/usr/bin/python
# -*- coding: utf-8 -*-

# 作者: itdeer
# 时间: 2019/3/28

f = open("demo2", "a")
print(f.fileno())
f.write("\n gggg")

f.close()