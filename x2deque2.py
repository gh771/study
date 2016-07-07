#!/usr/bin/python
# -*- coding:  utf-8  -*-

#有两种方法可以实现双端队列ADT，使用内建类型list，使用标准库collections.deque(其实collections.deque就是python中双端队列的标准实现)
# 1使用内建类型list
#front(前面) rear(后方的) empty(空的) size(大小)

class Deque():
	def __init__(self):
		self.items = []
	def addFront(self, items):
		self.items.insert(0, items)#insert(index, obj)函数用于将制定对象插入到列表指定位置
	def addRear(self, items):
		self.items.append(items)
	def removeFront(self):
		return self.items.pop(0)
	def removeRear(self):
		return self.items.pop()
	def empty(self):
		return self.size() == 0
	def size(self):
		return len(self.items)

de = Deque()
print(de.addFront(33,), de.addRear(44,), de.empty(), de.size())#None None False 2
print(de.items) #[33, 44]
print(de.addFront(22), de.addRear(55), de.addRear(11))
print(de.items)# [22, 33, 44, 55, 11]
print(de.removeFront())#22
print(de.removeRear())#11
print(de.items)#[33, 44, 55]

# 2使用标准库 collections.deque

from collections import deque

class deques():
	def __init__(self):
		self.items = deque()
	def addFront(self, item):
		self.items.appendleft(item)
	def addRear(self, item):
		self.items.append(item)
	def removeFront(self):
		return self.items.popleft()
	def removeRear(self):
		return self.items.pop()
	def empty(self):
		return self.size() == 0
	def size(self):
		return len(self.items)



print('------------------------------------------回文(palindrome)----------------------------------------------------')


#回文(palindrome)时正反读都一样的单词或句子，是一种修辞方式和文字游戏
#要实现一个回文验证算法使用Deque类非常容易，将字符串储存到双端队列，同时取出首尾字符并比较是否相等

def palchecker(aString):
	chardeque = Deque()
	for ch in aString:
		chardeque.addRear(ch)
	while chardeque.size() > 1:
		frist = chardeque.removeFront()
		last = chardeque.removeRear()
		if frist != last:
			return False
		return True
if __name__ == '__main__':
	str1 = 'able was i ere i saw elba'
	print('"%s" is%s palindrome' % (str1, '' if palchecker(str1) else ' not'))
	str2 = u'人人为我、我为人人'
	print(u'"%s"%s是回文' % (str2, u'' if palchecker(str2) else u'不'))
	str3 = u"What's wrong 怎么啦"
	print(u'"%s"%s是回文' % (str3, u'' if palchecker(str3) else u'不'))

str1 = 'able was i ere i saw elba'
str2 = u'人人为我、我为人人'
str3 = u"What's wrong 怎么啦"

strn=[str1,str2,str3]
for string in strn:

	print(" %s is %s palchecker" %(string, u''if palchecker(string)  else 'no'))

'''
able was i ere i saw elba is  palchecker
 人人为我、我为人人 is  palchecker
 What's wrong 怎么啦 is no palchecker'''







 
