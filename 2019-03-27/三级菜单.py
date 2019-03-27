#!/usr/bin/python
# -*- coding: utf-8 -*-

# 作者: itdeer
# 时间: 2019/3/27

address = {
    "浙江省":
        {
            "杭州市": {
                "西湖区": {
                    "工商大学": {},
                    "浙江大学": {},
                    "财经大学": {},
                    "工业大学": {}
                },
                "上城区": {
                    "银泰百货": {},
                    "全季酒店": {},
                    "天风商厦": {},
                    "金逸影城": {}
                },
                "下城区": {
                    "三里新城": {},
                    "和平广场": {},
                    "置业大厦": {},
                    "流水西苑": {}
                },
                "萧山区": {
                    "三江商厦": {},
                    "湘云雅苑": {},
                    "滨河中学": {},
                    "西兴中学": {}
                }
            },
            "宁波市": {
                "江北区": {
                    "中央花园": {},
                    "中山广场": {},
                    "黄金水岸": {},
                    "白沙医院": {}
                },
                "北仑区": {
                    "北仑电大": {},
                    "里仁花园": {},
                    "黄山豪庭": {},
                    "世贸花园": {}
                },
                "镇海区": {
                    "东海路": {},
                    "中宫路": {},
                    "俞范路": {},
                    "镇骆路": {}
                },
                "奉化区": {
                    "同山": {},
                    "提灯山": {},
                    "梅山": {},
                    "牛鼻山": {}
                }
            }
         },
    "河南省":
        {
            "郑州市": {
                "金水区": {
                    "海洋馆": {},
                    "农业大学": {},
                    "水利水电大学": {},
                    "动物园": {}
                },
                "二七区": {
                    "二七政府": {},
                    "航空航天大学": {},
                    "国资大厦": {},
                    "交通职业大学": {}
                },
                "惠济区": {
                    "大河广场": {},
                    "天伦庄园": {},
                    "格力广场": {},
                    "民安北郡": {}
                },
                "新郑区": {
                    "炎黄广场": {},
                    "黄帝故里": {},
                    "金湖广场": {},
                    "金鑫广场": {}
                }
            },
            "洛阳市": {
                "西工区": {
                    "名门万象": {},
                    "芳林大厦": {},
                    "居然之家": {},
                    "智联大厦": {}
                },
                "涧西区": {
                    "蓬莱小区": {},
                    "龙五社区": {},
                    "龙西社区": {},
                    "牡丹公园": {}
                },
                "老城区": {
                    "绿都": {},
                    "春园": {},
                    "清源": {},
                    "定鼎": {}
                },
                "新城区": {
                    "天明城": {},
                    "翡翠城": {},
                    "商会城": {},
                    "隆安城": {}
                }
            }
        }
}


current_address = address
up_address = []

while True:

    for i in current_address:
        print(i)
    choice = input(">>").strip()
    if len(choice) == 0:
        continue
    if choice in current_address:
        up_address.append(current_address)
        current_address = current_address[choice]
    elif choice == "b":
        if up_address:
            current_address = up_address.pop()
    elif choice == "q":
        break
    else:
        print("没有此选项")
