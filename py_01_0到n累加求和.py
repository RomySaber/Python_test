"""
-*- coding: utf-8 -*-
@Author  : Romy
@Time    : 2018/10/31 9:12
@Software: PyCharm
@File    : 累加求和

"""

result = 0
i = 0
num = int(input('请输入一个大于0的整数用于累加求和'))

while i <= num:
    result = result + i
    i = i + 1
print('0~ %d 之间数字的求和结果 = %d' % (num , result))
