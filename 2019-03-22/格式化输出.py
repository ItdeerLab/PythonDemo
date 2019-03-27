#!/usr/bin/python
# -*- coding: utf-8 -*-

# 作者: itdeer
# 时间: 2019/3/22


name = input("Name:")
age = int(input("Age:"))
job = input("Job:")
salary = input("Salary:")


if salary.isdigit():
    salary = int(salary)
# else:
#     exit("Age not digit")



msg = '''

------ info of %s ------
Name: %s
Age: %d
Job: %s
Salary: %f
------ end ------
''' % (name,name,age,job,salary)

print(msg)