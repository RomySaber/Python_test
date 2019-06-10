"""
-*- coding: utf-8 -*-
@Author  : Romy
@Time    : 2018/11/6 15:18
@Software: PyCharm
@File    : 封装九九乘法表

"""


# 封装
def multiple_table():
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            # print("*",end='')
            # 左对齐
            # print('%d * %d = %2d ' % (col, row, col * row), end='\t')
            # 右对齐
            print('%d * %d = %2d ' % (col, row, col * row), end='')
            col += 1
        print('')
        row += 1


# 调用(在其他文件中调用时需先import)
multiple_table()
