#!/usr/bin/python
# -*- coding:  utf-8  -*-

#双端队列(double-ended queue) #在需要按照元素增加的顺序来移除元素时非常有用
#能够有效的在开头（左侧）增加和弹出元素在列表无法实现
#双端队列通过可迭代对象创建,在collections模块它包括deque类型



from collections import deque

q = deque(range(5))# 创建双端队列
q.append(5) #队列在末尾加入5
q.appendleft(6)#在最左侧加入6
print(q)#deque([6, 0, 1, 2, 3, 4, 5])

print(q.pop())# 5 删除末端元素
print(q.popleft())#6  删除开头元素
print(q) #deque([0, 1, 2, 3, 4])

#使用rotate能够有效的旋转(rotate)元素，将他们左移或右移
#负值代表左移#默认是值为1
q.rotate() 
print(q) #deque([4, 0, 1, 2, 3])

q.rotate(3)#右移3位
print(q)#  deque([1, 2, 3, 4, 0])

q.rotate(-1)#左移1位
print(q)# deque([2, 3, 4, 0, 1])
