#!/usr/bin/python3
# -*- coding:  utf-8  -*-

# time模块常用方法
import time
#在不同系统上含义不同，在UNIX系统上，它返回的是'进程时间'，用秒表示的浮点数(时间戳)
#  而在windows中 第一次调用返回的是进程运行时间，而第二次之后的调用是自第一次调用以后到现在的运行时间
#实际上是以 WIN32 上Query Performance Counter(查询性能计数器) 为基础，它比毫秒更为精确

if __name__ == "__main__":
	time.sleep(1)
	print("clock1: %s" % time.clock())
	time.sleep(1)
	print("clock2: %s" % time.clock())
	time.sleep(1)
	print("clock3: %s" % time.clock())
'''
clock1: 0.019991
clock2: 0.020182
clock3: 0.02035'''

#线程推迟指定的时间运行，适合放在脚本里定时 time.sleep()
'''
while True:
	time.sleep(2)
	print(time.strftime('%H: %M: %S'))

15: 48: 08
15: 48: 10
15: 48: 12
15: 48: 14
15: 48: 16
15: 48: 18
15: 48: 20..........'''

print('--------------------------------timeit()-------------------------------------------')


#测试一段代码的运行时间，在python里面有个很简单的方法就是使用timeit模块
#timeit模块主要时timeit 和repeat 这两个函数

''''
timeit函数
timeit(stmt='pass', setup='pass', timer=<defaulttimer>, number = 10000)
返回执行 stmt 这段代码 number遍所用的时间，单位为秒，float类型

参数 stmt：要执行的那段代码 ， setup：执行代码的准备工作不计入时间，一般是import之类的
timer： 这个在win32下是time.clock(), linux下是time.time()，默认的不用管
number： 要执行 stmt 多少遍


repeat函数
repeat(stmt='pass', setup='pass', timer=<defaulttimer>, repeat=3, number= 10000)
这个函数比timeit函数多了一个repeat参数而已， 它表示重复执行timeit这个过程多少遍，
返回一个列表 表示执行每遍的时间
'''''


import timeit
import pprint
import math


def myfun():
	for i in range(100):
		for j in range(2,10):
			math.pow(i, 1/j)# math模块pow函数，pow(x,y) x的y次方

n= 100

t1 = timeit.timeit(stmt=myfun, number=n)
pprint.pprint(t1)# 0.04831360899970605

t2 = timeit.repeat(stmt=myfun, number=n, repeat=5)
pprint.pprint(t2)
'''
[0.04443236700080888,
 0.04424802199991973,
 0.044208616000105394,
 0.04437700099970243,
 0.04861188300037611]'''



print('------------------------------------------------------------------------------------------')

timeitobj = timeit.Timer(stmt=myfun)
t3 = timeitobj.timeit(number=n)
pprint.pprint(t3)# 0.04536546799954522

t4 = timeitobj.repeat(number=n, repeat=5)
pprint.pprint(t4)
'''
[0.04611412099984591,
 0.04453388099955191,
 0.044464775000051304,
 0.04458633499962161,
 0.04467696999927284]'''

print('----------------------------------------------------------------------------------------------')
class secs():
	def __init__(self, k=2, v=3):
		self.k= k
		self.v= v
		self.result = []
	def __next__(self):
		self.k, self.v = self.v, self.k+self.v
		return self.k
	def __iter__(self):
		return self


tt = timeit.timeit(stmt= secs, number=10)
print(tt)# 1.1363999874447472e-05

ty = timeit.repeat(stmt=secs, number = 10, repeat=5)
print(ty)

#[9.647999831940979e-06, 8.959999831859022e-06, 8.858000001055188e-06, 8.881999747245573e-06, 8.877000254869927e-06]















