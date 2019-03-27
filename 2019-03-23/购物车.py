#!/usr/bin/python
# -*- coding: utf-8 -*-

# 作者: itdeer
# 时间: 2019/3/23

# 输入资产
flag = True
while flag:
    salary = input("请输入您当前的工资:")
    if salary.isdigit():
        salary = int(salary)
        flag = False
    else:
        print("您输入的工资格式不对，重新输入...")


print("您当前的资产是: %d %s" % salary, "元")

# 商品列表
products = [('Mac', 8000), ('Kindle', 700), ('Tesla', 800000), ('PythonBook', 90), ('Bike', 3000)]
shopping_car = []

# 循环产品进行购买
while True:
    for i, v in enumerate(products, 1):
        print(i, ">>>", v)
    choice = input("选择购买的商品的编号[退出 请输入q]:")

    if choice.isdigit():
        choice = int(choice)
        if 0 < choice < len(products):
            p_item = products[choice - 1]
            if p_item[1] < salary:
                salary = salary - p_item[1]
                shopping_car.append(p_item)
                print("您购买的 %s 已加入购物车" % p_item[0])
            else:
                print("您的余额不足 还剩余 %d " % salary)
        else:
            print("编号不存在")
    elif choice == "q":
        print("------您已经购买如下的商品------")
        for i in shopping_car:
            print(i)
        print("还剩余 %d 元" % salary)
        break
    else:
        print("输入的编号不正确")
