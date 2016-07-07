#!/usr/bin/python
# -*- coding: latin-1 -*-

#python堆 heapq

#给出N长的序列， 求出TOPK大的元素使用小堆顶，heapq模块实现
import heapq
import random

class TopkHeap(object):
	def __init__(self, k):
		self.k = k
		self.data = []
	def Push(self, elem):
		if len(self.data) < self.k:
			heapq.heappush(self.data, elem)
		else:
			topk_small = self.data[0]
			if elem > topk_small:
				heapq.heapreplace(self.data, elem)
	def Topk(self):
		return [x for x in reversed([heapq.heappop(self.data) for x in range(len(self.data))])]
					#reversed函数反向排序 #heappop弹出self.data最小元素# 重复3次

if __name__ == '__main__':
	print("hello")
	list_rand = random.sample(range(1000000),10)# random模块sample(seq,n)从序列中选择n个随机且独立的元素
	th = TopkHeap(3)#创建实例对象th
	for i in list_rand:
		th.Push(i)#调用方法Push
	print(th.Topk())			#下标取前4
	print(sorted(list_rand, reverse=1)[:4])#sorted函数reverse参数为True或1时进行降序排列,为0或False默认时为升序排列
	print(sorted(list_rand))

#hello
#[940654, 915480, 883569]
#[940654, 915480, 883569, 808474]
#[114787, 170044, 425132, 612810, 613663, 738724, 808474, 883569, 915480, 940654]

print("---------------------------------------------------------------------------------------------------")

#给出N长的序列，求出BtmK 小的元素，即使用大堆顶
#heapq 在实现的时候，没有给出一个类似java的Compartor函数接口或比较函数，有人想出了很NB的思路
#在存入堆，从堆中取出的时候都用相反数，而其他逻辑与TopK完全相同
#即 push(e)改为push(-e), pop(e)改为-pop(e)


class BtmkHeap(object):
	def __init__(self, k):
		self.k = k
		self.data= []
	def Push(self, elem): #Reverse elem to convert to max-heap #逆元素转换为最大堆
		elem = -elem #Using heap algorighem #采用堆算法
		if len(self.data) < self.k:
			heapq.heappush(self.data, elem)
		else:
			topk_small = self.data[0]
			if elem > topk_small:
				heapq.heapreplace(self.data, elem)# 将堆中最小元素弹出，将elem入堆
	def Btmk(self):
		return sorted([-x for x in self.data])# x取反进行原地排序

if __name__ == "__main__":
	print('world')
	lrand = random.sample(range(1000000), 10)
	th = BtmkHeap(3)
	for i in lrand:
		th.Push(i)
	print(th.Btmk())
	print(sorted(lrand, reverse=False)[0:3])
	print(lrand)


#world
#[106783, 285042, 324254]
#[106783, 285042, 324254]
#[324254, 585111, 418916, 682926, 285042, 106783, 430182, 540297, 452368, 866820]





