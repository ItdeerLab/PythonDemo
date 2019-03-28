#!/usr/bin/python
# -*- coding: utf-8 -*-

# 作者: itdeer
# 时间: 2019/3/28

import time

f = open("demo1", "a")
print(f.fileno())

f.write("sss")

f.flush()

time.sleep(20)

f.close()