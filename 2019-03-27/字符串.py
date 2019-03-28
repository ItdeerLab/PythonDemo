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
print("dddd".ljust(10, "D"))  # 返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。
print("dddd".rjust(10, "D"))  # 返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串
print("DFee".lower())  # 转换字符串中所有大写字符为小写.
print("   dff".lstrip())  # 截掉字符串左边的空格或指定字符。

print("jksdk**jhdsf".partition("**"))  # 使用给定的分隔符将字符串划分为三个部分。这将搜索字符串中的分隔符。如果找到分隔符，返回一个三元组，其中包含分隔符前的部分，即分隔符本身，以及后面的部分。如果没有找到分隔符，则返回包含原始字符串的3元组和两个空字符串

print("Hello World".replace("ll", "pp"))  # 把 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。
print("Hello World".rfind("o"))  # 类似于 find()函数，不过是从右边开始查找.
print("Hello World".rindex("d"))  # 类似于 index()，不过是从右边开始.

print("dssd fffd   ".strip())  # 删除字符串字符串末尾的空格
print("Hello World".split(" "))  # num=string.count(str)) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num+1 个子字符串
print("Hello\r World".splitlines())  # 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
print("Hello World".startswith("He"))  # 检查字符串是否是以指定子字符串 substr 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查
print("Hello World".swapcase())

print("ttt".title())  # 返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
print("Hello World".translate("ld"))  # 根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中

print("Hello World".upper())  # 转换字符串中的小写字母为大写
print("Hello World".zfill(23))  # 返回长度为 width 的字符串，原字符串右对齐，前面填充0


tmp = "Heel Deep"

print(tmp[0])
print(tmp[1:6])
print(tmp[1:6:2])

print("\a")

print(r'\n')
print(R'\n')


print("Hello hh {} ll {}".format("aa", "dd"))
print("Hello hh {aa} ll {bb}".format_map({"aa":"KK", "bb":"RR"}))


print("2".maketrans("3", "4"))
