# -*- coding:  utf-8  -*-


#shelve:该模块可以创建持续性映射，同时将映射的内容保存在给定文件名的数据库中
#shelve模块 如果只需要一个简单的存储方案那么shelve模块可以满足大部分需求
#shelve模块中的open函数在调用它的时候(使用文件名作为参数)，它会返回一个shelf对象可以用它来存储内容
#只需要把它当作普通的字典来操作即可，在完成工作后调用close()方法

#潜在的陷阱

import shelve 

s = shelve.open("/home/how/test1/t2.txt")# 为open函数提供路径并创建一个文档
s['x'] = ['a', 'b', 'c', 'd']
s['x'].append('e')
print(s['x'])# ['a', 'b', 'c', 'd']
# 'e'没有出现，'e'没有写回把[abcd]存到了x ，当再次读取s['x']的时候,s['x']只是一个拷贝
#而没有将拷贝写回，所以再次读取s['x']的时候，它又从源中读取了一个拷贝， 所以新的内容不会出现在拷贝中
# 解决的第一个办法就是 利用一个缓存的变量
temp = s['x']
temp.append('e')
s['x'] = temp
print(s['x'])#['a', 'b', 'c', 'd', 'e']

#在python2.4以后的版本有了新方法，将 ope的参数writeback参数设为True
#如果这样做 所有从shelve读取或者赋值到shelf的数据都会保存到缓存中(cache),并且只有在关闭shelf的时候
#才会写回到磁盘，如果处理的数据不大 那么将writeback设为True(并在最后确保关闭了shelf)的方法还是不错的

t = shelve.open("/home/how/test1/t2",writeback = True)
t['y'] = ['w', 'x', 'y', 'z']
t['y'].append('u')
print(t['y']) #['w', 'x', 'y', 'z', 'u']

print('----------------------------------一个简单的数据库应用----------------------------------')

# -*- coding:  utf-8  -*-

#一个简单的使用shelve模块的数据库应用
import shelve, sys

def store_person(db): #Query user for data and store it the shelf object(查询用户数据并将其存储在“现成对象”中)
	pid = input("Enter unique ID number: ")
	person = {}
	person['name'] = input("Enter name: ")
	person['age'] = input("Enter age: ")
	person['phone'] = input("Enter phone number: ")
	
	db[pid] = person #在文档中储存数据创建字典

def lookup_person(db): #Query user for ID and desired dield, and fatch the corresponding data from(身份证查询用户所需的场，和他相应的数据)
	pid = input("Enter ID number: ")
	field = input("What would you like to know? (name, age, phone) ")
	field = field.strip().lower()   #字符串方法strip()返回去除两侧空格的字符串
	print(field.capitalize() + ':' ,  #lower()返回字符转小写字母版
	db[pid][field])      #capitalize()将字符串的首字母变成大写，其余小写

def print_help():
	print("The available commands are:")
	print("store : Stores information about a person")
	print("lookup : Looks up a person from ID number")
	print("quit : Save changes and exit")
	print("? : Prints this message")

def enter_command():
	cmd = input("Enter command (? for help): ")
	cmd = cmd.strip().lower()
	return cmd

def main():
	database = shelve.open("/home/how/test1/t3", writeback = True)#创建文档，writeback参数为True关闭文件时写回文档
	try:
		while True:
			cmd = enter_command()
			if cmd == "store":
				store_person(database)
			elif cmd == "lookup":
				lookup_person(database)
			elif cmd == '?':
				print(print_help())
			elif cmd == 'quit':
				return 
	finally:
		database.close()#使用finally确保数据库正常关闭，避免文件损坏
if __name__ == '__main__':
	main()
