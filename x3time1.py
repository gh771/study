#!/usr/bin/python3
# -*- coding:  utf-8  -*-
#time 模块所包含的函数能够实现以下功能，获得当前时间、操作时间爱呢和日期、从字符串读取时间以及格式化时间为字符串
#python中时间日期格式化符号%y 
# %y两位数的年份表示（00-99）    %Y 四位数的年份表示（000-9999）  %m月份（01-12）          %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）   %I 12小时制小时数（01-12）      %M 分钟数（00=59）         %S 秒（00-59）
# %a 本地简化星期名称         %A 本地完整星期名称             %b 本地简化的月份名称      %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示  %j 年内的一天（001-366）    %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53)星期天为星期的开始    %w星期(0-6)星期天为星期的开始   %W一年中的星期数(00-53)星期一为星期的开始
# %x 本地相应的日期表示      %X 本地相应的时间表示         %Z 当前时区的名称     %% %号本身 


import time 

#返回当前时间戳 (从新纪元1月1日开始计算到现在的秒数，每个平台的可能不同)UTC（Coordinated Universal Time，世界协调时）
#亦即格林威治天文时间，世界标准时间。在中国为UTC+8。DST（Daylight Saving Time）即夏令时。
#.时间戳（timestamp）的方式：通常来说，时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量。
#我们运行“type(time.time())”，返回的是float类型。返回时间戳方式的函数主要有time()，clock()等。

print("--------------------------time() localtime()-----------------------------------------------------")
#time.time() #返回当前时间戳 
print(time.time())#1467006878.0391085

#time.localtime([secs]) #将时间戳秒数转换为时间元组 #ruguo secs参数未提供则当前时间为准
print(time.localtime(1467006878.0391085))
#time.struct_time(tm_year=2016, tm_mon=6, tm_mday=27, tm_hour=13, tm_min=54, tm_sec=38, tm_wday=0, tm_yday=179, tm_isdst=0)

print(time.localtime())
#time.struct_time(tm_year=2016, tm_mon=6, tm_mday=27, tm_hour=14, tm_min=6, tm_sec=48, tm_wday=0, tm_yday=179, tm_isdst=0)

print("-------------------------------gmtime() mktime()-----------------------------------------------------")
#time.gmtime([secs]) #和localtime()方法类似,gmtime()方法将一个时间戳转换为UTC时区(0时区)

print(time.gmtime())
#time.struct_time(tm_year=2016, tm_mon=6, tm_mday=27, tm_hour=6, tm_min=10, tm_sec=21, tm_wday=0, tm_yday=179, tm_isdst=0)

print(time.gmtime(1467006878.0391085))
#time.struct_time(tm_year=2016, tm_mon=6, tm_mday=27, tm_hour=5, tm_min=54, tm_sec=38, tm_wday=0, tm_yday=179, tm_isdst=0)

#time.mktime(tuble) # 将时间元组转换为时间戳秒数
print(time.mktime(time.localtime())) #1467008225.0
print(time.mktime((2016,6, 27, 5, 54,38, 0, 179, 0)))# 1466978078.0

print("--------------------------------------asctime() ctime()---------------------------------------------")
#time.asctime([tuple]) # 将时间元组转换为时间字符格式, 如果没有参数将time.localtime()作为默认参数
print(time.asctime()) #Mon Jun 27 14:20:43 2016

# time.ctime([secs]) # 将时间戳转换为字符转格式 参数为空时默认 time.time() 为参数
print(time.ctime())#Mon Jun 27 14:32:45 2016

print("------------------------------------sleep() clock() --------------------------------------------------")

# time.sleep(secs) 线程推迟指定的时间运行 单位为秒
print(time.sleep(3))
print("time.sleep() Test")# time.sleep() Test

# time.clock() # 在不同系统上含义不同，在UNIX系统上，它返回的是'进程时间'，用秒表示的浮点数(时间戳)
	       # 而在windows中 第一次调用返回的是进程运行时间，而第二次之后的调用是自第一次调用以后到现在的运行时间
		#实际上是以 WIN32 上Query Performance Counter(查询性能计数器) 为基础，它比毫秒更为精确
print(time.clock())# 0.020266

print('------------------------------strptime() strftime()---------------------------------------------------')
# time.strptime(string,[, format]) # 将时间字符串解析为时间元组struct_time
#print(time.strptime(time.ctime()))
#print(time.strptime(time.asctime()))
#time.struct_time(tm_year=2016, tm_mon=6, tm_mday=27, tm_hour=14, tm_min=55, tm_sec=53, tm_wday=0, tm_yday=179, tm_isdst=-1)
print(time.strptime('Mon Jun 27 14:52:41 2016'))
#time.struct_time(tm_year=2016, tm_mon=6, tm_mday=27, tm_hour=14, tm_min=52, tm_sec=41, tm_wday=0, tm_yday=179, tm_isdst=-1)


#time.strftime()# 根据指定的格式化字符输出默认为当前时间, t未指定传入time.localtime() 作为默认参数


print(time.strftime("%Y-%m-%d %H:%M: %S"))# 2016-06-27 15:39: 02
print(time.strftime("%y- %M-%D %h:%m:%s"))# 16- 44-06/27/16 Jun:06:1467013472
























