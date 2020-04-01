# 双引号


# 转义字符

# 原始字符串
'''
在单引号之前加上r，使其成为原始字符串
'''

print(r'That is Carol\'s cat.') 

# 用三重引号的多行字符串

# 多行注释
"""
	多行注释
	多行注释
"""

# 字符串下标和切片
spam = 'Hello world!'
spam[0:5]

# 字符串的in和not in操作符
>>> 'Hello' in 'Hello world'
True

# 字符串方法

upper() 
lower()
isupper()
islower()

# isX方法
isalnum() # 字符和数字
isalpha() # 字母
isspace() # 空格
istitle() # 首字母大写
isdecimal() #  判断是否只包含数字字符


'''
这些方法在判断用户输入时很有用处
'''

startswith()
endswith()

join() # 输入是列表，输出是字符串。调用join()方法的字符串，被插入到列表参数中的每个字符串的中间。
'''

>>> ' '.join(['My', 'name', 'is', 'Simon'])
'My name is Simon'

'''
split() # 输入是字符串，输出是列表。 参数是分隔符，输出列表的元素是每个被分隔符分割的部分。
'''

>>> ' '.join(['My', 'name', 'is', 'Simon'])
'My name is Simon'

'''

# 字符串对齐

rjust()
ljust()
center()


strip() # 去掉首尾空格
rstrip() # 去掉开头空格
lstrip() # 去掉尾部空格
# 有个可选参数
>>> spam = 'SpamSpamBaconSpamEggsSpamSpam'
>>> spam.strip('ampS')
'BaconSpamEggs'

# 使用pyperclip模块拷贝粘贴字符串






























