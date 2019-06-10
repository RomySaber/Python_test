"""
-*- coding: utf-8 -*-
@Author  : Romy
@Time    : 2018/10/28 9:14
@Software: PyCharm
@File    : if嵌套

"""

# 定义布尔变量 has_ticket 表示是否有车票
has_ticket = True

# 定义浮点型变量 knife_length 表示刀的长度，单位为厘米
knife_length = 19.5

# 首先检查是否有车票，如果有才允许进入安检
if has_ticket:
    print('车票检查通过，准备进入安检')

    # 安检时检查刀的长度，判断是否超过20厘米
    if knife_length > 20:
        # 如果超过20厘米，提示刀的长度，不允许上车
        print('您携带的刀太长了，有 %f 厘米长' % knife_length)
        print('不允许上车')
    # 如果不超过20厘米，安检通过
    else:
        print('安检通过，祝您旅途愉快！')

# 如果没有车票，不允许进门
else:
    print('无车票，不允许进入！')
