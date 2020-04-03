#!python

\d{3}-\d{3}-\d{4}

import re
'''
re.compile() 传入一个正则表达式字符串，它将返回一个Regex对象
'''
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}') # phoneNumRegex 变量包含一个Regex对象

mo = phoneNumRegex.search('My number is 415-555-4242.')

# search() 方法返回一个Match对象。Match对象一个group()方法。
mo.group() # 打印匹配到的内容
# 分组
phoneNumRegex1 = re.compile(r'(\d\d\d)-(\d{3}-\d{4})') # 第一对括号表示第一组
mo = phoneNumRegex.search('My number is 415-555-4242.')
mo.group(1)
mo.group(2)
# 管道符 |
heroRegex = re.compile(r'Batman | Tina Fey')