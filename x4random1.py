#!/usr/bin/python3
# -*- coding:  utf-8  -*-

'''randon模块包括返回随机数的函数，可以用于模拟或者用于任何产生随机输出的程序
事实上所产生的数字都是伪随机数也就是说它们看起来是完全随机的，但实际上它们以一个可与测的系统作为基础
如果需要真的随机性应该使用OS模块的urandom函数，random模块内的SystemRandom类也是基于同种功能
可以让数据接近真正的随机性'''
import random

print('--------------------------------random() getrandbits(n)------------------------')
#random.random() #用于生成0-1的随机浮点数
print(random.random())# 0.6284596648947305

#random.getrandbits(n) #以长整型形式返回给定的n个随机位（二进制数），如果处理的是真正的随机事务(比如加密)，这个函数尤为有用

print(random.getrandbits(33))#1046314498  
print(random.getrandbits(133))#9747365958653834010680526451730960106582

print('------------------uniform(a,b), randrange([start], stop, [step]), randint(a,b)--------------')

#random.uniform(a,b) # 用于生成指定范围的随机浮点数，两个参数其中一个是上限一个是下限，a<= n <b
print(random.uniform(1,100))#40.15428329583848
print(random.uniform(100,1))#97.07810095050503
print(random.uniform(0,360)) #随机的角度值 234.84926675422076

#random.randrange([start], stop, [step]) #返回从指定范围内，按指定基数递增的集合中获取一个随机数
                    #起始 停止 步长
print(random.randrange(1,10))#8 1至10的随机数
print(random.randrange(10)+1)#6
print(random.randrange(1,20,2))#7 获得小于20的随机正奇数

#random.randint(a,b)# 用于生成一个指定范围内的整数，a是下限b是上限下限必须小于上限，生成随机数n: a<= n <=n

print(random.randint(1,100))#12
print(random.randint(10,10))#10 #结果永远是10
try:
	print(random.randint(100, 1))#该语句是错误的，下限必须小于上限
except Exception as e:
	print("Error is :",e)# Error is: empty range for randrange() (100,2, -98)

print('-----------------------choice(seq), shuffle(seq[,random])--------------------')

#random.choice(seq) # 从序列中返回一个随机元素，参数seq(sequence)表示一个有序类型，
#sequence在python中不是一种特定类型，而是泛指一系列的类型，list tuple 字符串都属于sequence
s1 = "学习 python"
s2 = " 'The', 'ice', 'is', 'too','thin', to bear your weight"
s3 = ['Somescientists' ,'experiment','on','animals']

print(random.choice("Don't excite yourself"))# l
print(random.choice(s1))#习
print(random.choice(s3))# on

#random.shuffle(seq[,random]) #将给定的(可变)序列中的元素进行原地随机移位，每种排序的可能性都是近似相等的

s4 = ['two', 2,'days','天', 'before christmas']

 
random.shuffle(s3) #进行原地随机移位
random.shuffle(s4)
print(s3,s4) #['animals', 'experiment', 'Somescientists', 'on']  ['days', '天', 'two', 'before christmas', 2]


print('--------------------------sample(seq, n)----------------------------------')
#random.sample(seq, n) #从给定的序列中(均一的)选择给定数目的元素，同时确保元素互不相同
l1 = [1,2,3,4,5,6,7,8]
l2 = ['make','song','popular', 'have','a','scarf','around','my','neck']

print(random.sample(l1,3))#[3, 4, 6]
ll = random.sample(l2,5)
print(ll)#['make', 'my', 'have', 'around', 'a']

ss = random.sample(s1,3)
print(ss)# ['习', 'y', ' ']

print(random.sample(s2,4))#[' ', ' ', 'o', ',']





















