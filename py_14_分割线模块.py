"""
-*- coding: utf-8 -*-
@Author  : Romy
@Time    : 2019/1/6 12:51
@Software: PyCharm
@File    : 14_分割线模块

"""


def print_line(char, times):
    print(char * times)


def print_lines(char, times):
    row = 0
    while row < 5:
        print_line(char, times)
        row += 1


# print_lines("-", 20)
name = 'Romy模块练习'
