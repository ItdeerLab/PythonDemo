#!/usr/bin/python
# -*- coding: utf-8 -*-

# 作者: itdeer
# 时间: 2019/3/27

str = "hello world"


print(str)

print(str.capitalize())  # 将第一个字符大写
print("Hello".casefold())  # 返回一个无大小写的版本字符串
print(str.center(60, "#"))  # 将字符串放中间，两边使用一个字符进行填充
print(str.count("ll", 2))  # 返回字符在整个字符串出现的次数，可以指定索引的开始和结束位置

print(str.find("w", 3))  # 返回所查找的字符的索引位置，可以指定索引开始和结束的位置
print("Hello hh".format("aa"))
# print(str.format_map())

print(str.isdigit())  # 判断是否为整数
print(str.index("o"))  # 返回字符在整个字符串的索引位置
print("qwe123".isalnum())  # 字符串中是否含有数字或者字符则返回True
print("qwe".isalpha())  # 如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
print("12".isdecimal())  # 检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false
print("12as_".isidentifier()) # 如果字符串是有效的Python标识符，则返回True，否则返回False
print("a".islower())  # 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
print("121".isnumeric())  # 如果字符串中只包含数字字符，则返回 True，否则返回 False
print("dd".isprintable())  # 如果字符串是可打印的，返回True，否则返回False。
print(" ss".isspace())  # 如果字符串中只包含空白，则返回 True，否则返回 False.
print("Asd Ass".istitle())  # 如果字符串是标题化的(见 title())则返回 True，否则返回 False
print("Dsss A".isupper())  # 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False

print("AAA".join("fff"))  # 以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串