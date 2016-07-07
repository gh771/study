# -*- coding:  utf-8  -*-
#------------------------------
 

'''匹配对象和组'''
#当找到匹配项的时候，它们会返回MatchObject对象，例如<_sre.SRE_Match object; span=(0, 6), match='Winter'>
#这些对象包括匹配模式的子字符串的信息，它们还包含了那个模式匹配字符串那部分的信息， 这些"部分"叫做组(group)
#简而言之 组就是放置元括号内的子模式，组的序号取决于它左侧的括号数，组0就是整个模式，最多能使用99个组

# group([group1,...]) #获取给定子模式(组)的匹配项
# start([group]) #返回给定组的匹配项的开始位置 ，默认为0
# end([group]) #返回给定组的匹配项的结束位置，返回结果是结束索引加1 ， (和分片一样不包括组的结束位置)
# span([group]) # 返回给定组的开始和结束位置的索引，默认为0 

import re 
m = "as smooth as mirror, Hear cries all around, Have a guess at the answer"
match1 = re.match(r'as (.+) as (.+?), ([a-z]{4}) cries all (.+?), Have (.{1}) (.{5}) (.+)', m, re.I|re.M)
if match1:
	print(match1.group()) #as smooth as mirror, Hear cries all around, Have a guess at the an
	print(match1.group(1))# smooth
	print(match1.group(2)) # mioor
	print(match1.group(3)) # Hear
	print(match1.start(4)) # 36
	print(match1.end(5)) # 50
	print(match1.span(6)) # (51, 56)
	print(match1.group(7)) # at the answer
else:
	print('not match')



#见证 re.sub强大功能的最简单的方式就是在替换字符串中使用组号

import re

str1 = "Hello , *world*! $have$ no doubt of his ability piano keyboard"

emphasis_pattern = r'\*([^\*]+?)\*'
emphasis = r'\$(\w+?)\$ ([a-z]{2}) (.+) ability'

print(re.sub(emphasis_pattern, r'</em>\1</em>', str1))#Hello , </em>world</em>! $have$ no doubt of his ability piano keyboard
print(re.sub(emphasis, r'</em>\1</em>', str1))#Hello , *world*! </em>have<e/m> pianokeyboard
print(re.sub(emphasis, r'</em>\2</em>', str1)) #Hello , *world*! </em>no</em> piano keyboard
print(re.sub(emphasis, r'</em>\3</em>', str1)) #Hello , *world*! </em>doubt of his</em> piano keyboard
print(re.sub(emphasis, r'XXX\3XXX', str1)) # Hello , *world*! XXXdoubt of hisXXX piano keyboard


