"""
-*- coding: utf-8 -*-
@Author  : Romy
@Time    : 2018/10/28 10:13
@Software: PyCharm
@File    : 石头剪刀布随机事件

"""
import random
# 从控制台输入要出的拳：石头（1）、剪刀（2）、布（3）
player = int(input('请输入您要出的拳：石头（1）、剪刀（2）、布（3）'))
# 电脑随机出拳
computer = random.randint(1,3)

print('玩家选择的拳是 %d - 电脑出的拳是 %d' % (player, computer))

# 比较胜负
# 1 石头 胜 剪刀
# 2 剪刀 胜 布
# 3 布 胜 石头
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print('欧耶，电脑弱爆了！')
# 平局
elif player == computer:
    print('真是心有灵犀啊，再来一盘！')

# 其他情况就是电脑获胜
else:
    print('电脑获胜！！！')
