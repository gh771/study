# -*- coding:  utf-8  -*-
# ------------------------------


print('-------------------------------寻找发信人程序','-'*10)
#在头部找到Emali地址，可以调用fileinput.close()因为头部不包括空行，
#此外还可以调用 fileinput.nextfile()开始处理下一个文件，如果文件多余一个的话

import re, fileinput
pat = re.compile('From: (.*) <.*?>$')# 将需要取出的子模式放在圆括号中作为组，非贪婪模式，使用$正行匹配
for line in fileinput.input('/home/how/test1/t4Email'):
	m = pat.match(line)
	if m: print(m.group(1))# Foo Fie #使用 if 确保在从特定组中取出匹配内容之前，的确进行了匹配
#     print(m.froup(1), fileinput.filelineno()) #Foo Fie 16




pat = re.compile(r'[a-z\-\.]+@[a-z\-\.]+',re.I) # re.IGNORECASE
addresses = set()# 为了避免重复将地址保存在集合中

for line in fileinput.input('/home/how/test1/t4Email'):
	for address in pat.findall(line):
		addresses.add(address)
		print(fileinput.filelineno(), '->', end='') #4 ->5 ->8 ->16 ->17 ->18 ->19 # 正则匹配所在行数
for address in sorted(addresses):
	#print(address)#原例   # 在排序的时候大写字母要比小写字母靠前
	print(address, end='') # Mr.Gumby@bar.bazfoo@bar.bazfoo@baz.commagnus@bozz.floop



print('-----------------------------模板--------------------------')

#模板 是一种通过放入具体值从而得到某种已完成文本的文件
#python 有一种高级的模板机制:字符串格式化， 但是使用正则表达式可以让系统更加高级

#exec(object[,globals[,locals]] 是一个语法声明可以执行动态字符串代码片段，两个参数用来指定执行代码使用的全局变量和局部变量 
#eval(expression[,globals,[,locals]])函数可以计算python表达式 并且返回结果,如果忽略后面两个参数，eval在当前作用域执行， 作用域必须是字典

print('-'*15, '一个简单的模板系统','-'*15)
import fileinput , re


field_pat = re.compile(r'\[(.+?)\]') #匹配方括号里的字段

scope = {} #将变量收集到这里

def replacement(match): #用于 re.sub中
	code = match.group(1)#将组1从匹配中取出放入code中，也就是两个方括号之间的字符
	try:
		return str(eval(code,scope))#如果字符串可以求职返回它 #The sum of [x] and [y] is [x+y]可以执行返回它
	except SyntaxError:
		exec (code,scope) #否则执行相同作用域scope内的赋值语句 执行 x=2 y=3 返回空字符串
		return '' #返回空的字符串

#将所有文本以一个字符串的形式获取
lines = []
for line in fileinput.input('/home/how/test1/t5'):
	lines.append(line)
text = ''.join(lines)
print(lines)
print(text)
#将field模式的所有匹配项都替换掉
print(field_pat.sub(replacement, text))# The sum of 2 and 3 is 5
#print(re.sub(field_pat, replacement, text))



print('------------------------------模板示例导入多个文件----------------------------------')

#因为使用了fileinput可以轮流处几个文件，这意味着可以使用一个文件为变量定义值，
#而另一个文件作为插入这些值的模板

import re, fileinput

field_pat = re.compile(r'\[(.+?)\]')

scope = {}

def replacement(match):
	code = match.group(1)
	try:
		return str(eval(code,scope))
	except SyntaxError:
		exec(code, scope)
		return ''

lines = []
for line in fileinput.input(['/home/how/test1/t6magnus.txt', '/home/how/test1/t7template.txt']):
	lines.append(line)
text = ''.join(lines)

print(field_pat.sub(replacement, text))
fileinput.close()



'''
#应用于x6re1模板示例



#应用x6re1模板示例


Dear Magnus Lie Hetland

I would like to learn how to program . I hear you use
the python language a lot -- is it something I
should consider?

And, by the way, is magnus@foo.bar your correct email address?

Fooville, Wed Jul  6 09:39:20 2016

Oscar Frozzbozz'''
