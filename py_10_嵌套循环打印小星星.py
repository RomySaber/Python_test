"""
-*- coding: utf-8 -*-
@Author  : Romy
@Time    : 2018/10/31 16:03
@Software: PyCharm
@File    : 嵌套循环打印小星星

"""

row = 1
while row <= 5:
    col = 1
    while col <= row:
        print("*",end='')
        col += 1
    print('')
    row +=1
