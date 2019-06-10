"""
-*- coding: utf-8 -*-
@Author  : Romy
@Time    : 2018/10/31 9:29
@Software: PyCharm
@File    : 0到n之间偶数求和

"""

result = 0
num = int(input('请输入一个大于0的数字用于累加求和：'))
i = 0
while i <= num:
    if i % 2 == 0:
        # print(i)
        result += i
    i += 1
print('0~ %d 之间偶数的求和结果 = %d' % (num, result))
