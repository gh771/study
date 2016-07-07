# -*- coding:  utf-8  -*-
#------------------------------

# re 模块包含对正则表达式(regular expression)的支持
#正则表达式是可以匹配文本片段的模式

# . 点号通配符可以匹配除了换行符(\n)以外的任意字符
# \ 转义(escape)符号 改变原来符号的含义
# [] 中括号用来创建一个字符集， 字符集可以匹配它所包含的任意字符， 
#如果在开头使用^字符 ['^abc'] 可以匹配除了abc以外的任意字符
# \d 匹配数字[0-9] # \D与小写相反匹配所有的非数字字符
# \s 匹配空白字符空格[\t\n\r\f\v] # \S 匹配非空白字符
# \w 匹配字母数字下划线汉字等[a-z][A-Z][0-9  # \W 匹配不是字母数字下划线汉字的内容
#\b 匹配字符的开始和结束
# ^ 匹配字符串的开始 # $匹配字符串的结束
# | 选择符 # （）子模式 # ()? 在子模式后加上问号？ 它就变成了可选子模式
# 重复模式  #(pattern)*允许模式重复0到多次 #(pattern)+允许模式重复1次或多次
# (pattern){m,n} #允许模式重复m-n次
print('------------------------------re所定义的flags参数包括-----------------------------------')
# re.I #忽略大小写  # re.L #表示特殊字符集 \w, \W, \b,\B, \s, \S 依赖于当前环境
# re.M #多行模式   #re.S #即为'.' 并且包括换行符在内的任意字符
# re.U # 表示特殊字符集 \w \W , \b \B, \d \D, \s \S 依赖于Unicode字符属性数据库
# re.X #为了增加可读性， 忽略空格和 '#' 后面的注释

print('--------------------------------re.compile(), re.search()------------------------------------')

import re 

# re.compile(pattern[, flags]) #编译正则将正则表达式转换为(RegexObject)模式对象可以实现更有效率的匹配
# 如果在调用search 或者match函数的时候使用字符串表示的正则表达式，它们也会在内部将字符串转换为正则对象
string = 'He could hardly fall asleep, Winter is almost over , old'
l = 'have no doubt of his ability, make a trip to the moon'
w = "Winter is almost over"
pat = re.compile(r'o(.){4}')

# re.search(pattern, string[, flags]) # 在字符串寻找第一个匹配给定的表达式，找到子模式函数返回MatchObject(匹配对象)
#如果不能匹配返回None, 因为返回值的性质，所以该函数可以应用在条件语句中

print(re.search(pat, string)) # <_sre.SRE_Match object; span=(4, 9), match='ould '>

if re.search(r'l(\w){2,3}', string):
    print("Found it") # Found it

print(re.search(r'l(\w){2,3}', string)) #<_sre.SRE_Match object; span=(23, 27), match='leep'>

print("---------------------re.match() re.split()-------------------------------------")
# re.match(pattern, string[, flags]) # 在给定字符串的开始处匹配模式, 如果不能匹配返回None，
# 如果要求匹配整个字符串，可以在模式的结尾上加上 $ 符号， 可以应用到条件语句中

print(re.match(r'h(\w){2,3}',w))# None

print(re.match(r'W(.){5}', w)) #  <_sre.SRE_Match object; span=(0, 6), match='Winter'>

# re.split(pattern,string[, maxsplit=0]) #根据模式的匹配项来分割字符串，类似字符串方法split，不过时用完整的正则代替了固定的分隔符
#参数 maxsplit是分离的次数，maxsplit=1分离1次，默认为0不限制次数,如果用括号将正则括起来，那么匹配的字符串会被列入到list中返回
string1 = "have a guess at the answer have a guess at the answer"
print(re.split(r'a.{1}', string1))# ['h', 'e ', 'guess ', ' the ', 'swer h', 'e ', 'guess ', ' the ', 'swer']
print(re.split(r'\s', string1))#['have', 'a', 'guess', 'at', 'the', 'answer', 'have', 'a', 'guess', 'at', 'the', 'answe
print(re.split(r'\s', string1, maxsplit = 2)) #['have', 'a', 'guess at the answer have a guess at the answer']

string2 = 'alpha, beta,,,, game delta'
print(re.split('[,]+', string2)) #['alpha', ' beta', ' game delta']
#如果模式包含小括号，那么扩起来的字符组合会散布在分割的子字符串之间
print(re.split('.(a)', string2))#['alp', 'a', ', be', 'a', ',,,, ', 'a', 'me del', 'a', '']


print('----------------------------findall() finditer()--------------------------------------')

# re.findall(pattern, string) #列出字符串中所有匹配项以列表形式返回，如果无匹配返回空
string3 = "manage to pass the examination 	Examination The Pass To Manage"
#
print(re.findall(r'[[A-Z]{1}[a-z]{2,3}', string3)) # ['Exam', 'The', 'Pass', 'Mana']
string4 = " 'HE', 'could', 'hardly', 'FALL', 'asleep' , '123', '456','789',"
print(re.findall('[A-Z]+', string4)) #['HE', 'FALL']
print(re.findall('[a-zA-Z]+', string4)) #['HE', 'could', 'hardly', 'FALL', 'asleep']

string5 = "/\|have @# no ,.doubt '...' ?: of !; his-- ability "
print(re.findall(r'[,.\'!\-?"\\\/\|]', string5)) #['/', '\\', '|', ',', '.', "'", '.', '.', '.', "'", '?', '!', '-', '-']

#re.finditer(pattern, string, flags=0) # 把所有模式匹配项作为一个迭代器返回
string6 =  "12 wthch 34 the 56 rise 78 of 90 the sun apear on  a  TV  program"
ite = re.finditer(r'\d{2}', string6)
import pprint
for i in ite:
	print(i.group(),end='') #1234567890

print("-----------------------------re.sub() re.escape()----------------------------------------")
	#pattern replace 
# re.sub(pat, repl, string[,count=0]) #将字符串中所有pat的匹配用repl替换掉，如果无匹配字符串无改变返回
#可选参数count是模式匹配后替换的最大次数，count必须时正整数，默认为0替换所有匹配项

string7 = "different 'methods', 'for' studying English Some scientists experiment on animals"
print(re.sub(r'o[a-z]+', 'three', string7))
#different 'meththree', 'fthree' studying English Sthree scientists experiment three animals

print(re.sub(r'[a-z]{3}', 'eight', string7, count = 8))
#eighteighteight 'eighteights', 'eight' eighteightng English Some scientists experiment on animals

''' re.excape(string) #对字符串中所有可能被解释为正则运算符的字符进行转义'''

string8 = "Don't .excite \yourself/, have |a *scarf +around? my neck"
string9 = "walk []through {}an() ancient foresr"
print(re.escape(string8))
#Don\'t\ \.excite\ \\yourself\/\,\ have\ \|a\ \*scarf\ \+around\?\ my\ neck
print(re.escape(string9))
# walk\ \[\]through\ \{\}an\(\)\ ancient\ foresr



