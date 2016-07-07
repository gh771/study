# -*- coding:  utf-8  -*-
#random模块应用示例


print("------------------------------获取随机日期---------------------------------")
from random import *# 将模块内容全部导入
from time import *

date1 = (2016, 1, 1, 0, 0, 0, -1, -1, -1)
time1 = mktime(date1)#将日期元组转换为秒数

date2 = (2017, 1, 1, 0, 0, 0, -1, -1, -1)
time2 = mktime(date2)

random_time = uniform(time1, time2)#返回 a b 间的随机实数

print(asctime(localtime(random_time)))#Sun Jan 10 04:45:17 2016#将秒数转换为日期元组，将日期元组转换为字符串

print("--------------------------------投掷骰子-----------------------------------")
#要求输入投掷骰子的个数以及每个骰子的面数

from random import randrange
num = int(input("How many dice? "))
sides = int(input("How many sides per die? "))

sum = 0
for i in range(num):
	sum += randrange(sides) +1

print("The result is: ", sum)# The result is:  13


print("---------------------------星座运势--------------------------------------")
#一个新建的文本文件，它的每一行文本都代表一种运势，那么就可以使用fileinput模块将"运势"存入列表内，再进行随机选择

import fileinput , random

fortunes = list(fileinput.input('/home/how/test1/t1'))
print(random.choice(fortunes))#金牛座2 吉星云集于3宫，

print("--------------------------发牌程序---------------------------")

import pprint


#假设你希望程序能够在每次敲击回车的时候都为自己发一张牌，同时还要确保不会获得相同的牌

#创建一副牌的字符串列表
values = list(range(1,11)) + 'Jeck Queen King'.split()# 10 + j-k
suits = "diamonds clubs hearts spades".split()# 花色
deck = ["%s of %s" %(v,s) for v in values for s in suits]

from random import shuffle# 导入shuffle函数 对deck中元素进行原地移位
shuffle(deck)
#pprint.pprint(deck[:9])#取前9张牌

while deck:
	input(deck.pop())





print("-----------------------生成随机验证码------------------------------")
import random
checkcode = ''
for i in range(4):
	current = random.randrange(0,4) #0-4的随机数
	if current !=i:
		temp = chr(random.randint(65,90))# 如果current不等于1,就把65-90的随机整数由chr转换为ASCII字符
	else:
		temp = random.randint(0,9)
	checkcode += str(temp)# checkcode等于'' 加上每次循环的字符串化str(temp)
print(checkcode)# 9URB # 循环4次生成4位的验证码

code = []
for i in range(6):
	if i == random.randint(1,5):
		code.append(str(random.randint(1,5)))#code加入str化的1-5的随机数
	else:
		temp = random.randint(65,90)
		code.append(chr(temp))#code列表加入temp转化后的ASCII字符

print(''.join(code))#EDH3DB  #循环6次用join函数连接列表code

print('--------------------------------------------------------------------------------')
#根据预订好的字符串，然后生成16位的随机密码
import random
#密码字符池
pwdstrpool = '0123456789'\
'abcdefghijklmnopqrstuvwxyz'\
'~@#$%^&*()+-*/='\
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'\


#密码字符串池长度
Size = len(pwdstrpool)

pwdlen = [16,16] #定义要生成的密码长度 #[0,16]0至16位

def Getrandomnum(p):# 获取一个随机数
	randomnum = random.randint(0, Size-1)
	return pwdstrpool[randomnum]

def Getrandompwd(pwdlen):#获取随机密码
	Randompwd = ''.join(map(Getrandomnum, range(pwdlen)))#map函数接受一个函数和一个可迭代对象作为参数，
	return Randompwd                                      #用函数处理每个元素，然后返回新的列表

def tester():
	print(Getrandompwd(random.randint(pwdlen[0], pwdlen[1])))# 可以改为Getrandompwd(16)

if __name__ == '__main__':
	tester()#PyQ++g#dkF0dcgX@


print("--------------------------chr(), unichr()， ord()--------------------------")
#这个函数和php里面的用法是一样的
#chr() #返回整数x对应的ASCII字符 参数取值范围在0-255之间的正整数，与ord(x)作用相反
print(chr(60), chr(90), chr(65), chr(75), chr(95), chr(115), chr(155), chr(185), chr(255))#< Z A K _ s  ¹ ÿ

'''
#unichr() #和chr()一样，只不过它返回的时Unicode字符，这个从python2.0才加入的unicode()的参数范围依赖于你的python是如何被编译的。
#如果配置为USC2的Unicode，那么它允许的范围就是range(65536)或0x0000-0xFFFF，
#如果配置为UCS4，那么这个值应该是range(1114112)或 0x000000-0x110000.
#如果提供的参数不在允许的范围内 则会报一个ValueError的异常
print(unichr(1),  unichr(30), unichr(60), unichr(90), unichr(120), unichr(255), unichr(500),unichr(65535))
print(unichr(1114111))'''


#ord()函数是chr()(对于8位的ASCII字符串) 或 unichr()函数(对于Unicode对象)的配对函数，
#它以一个字符(长度为1的字符串)作为参数，返回对应的ASCII数值，或者Unicode数值
#如果所给的Unicode字符超出了你的python定义范围，则会引发 一个TypeError的异常
print(ord('a'), ord('b'), ord('v'), ord('w'), ord('S'), ord('G')) #97 98 118 119 83 71
print(ord(u'\u2345'), ord(u'\u4e2d'))# 9029 20013


































