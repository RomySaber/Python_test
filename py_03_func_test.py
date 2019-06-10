"""
-*- coding: utf-8 -*-
@Author  : Romy
@Time    : 2018/10/12 15:34
@Software: PyCharm Community Edition
@File    : func_test.py
"""


# a = [1,2,3,4,5,6,7]
# list(filter(lambda x: x > 2, a))

def counter():
    cnt = [0]

    def add_one():
        cnt[0] += 1
        return cnt[0]

    return add_one()


num1 = counter()
print(num1)
print(num1)
