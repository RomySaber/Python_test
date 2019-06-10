"""
-*- coding: utf-8 -*-
@Author  : Romy
@Time    : 2018/11/2 16:04
@Software: PyCharm
@File    : 输出九九乘法表

"""

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
