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


#  口令保管箱

#!python
# pw.py -- managy your password.

PASSWORDS = {'email':'4rfv%TGB',
			'Blog':'7ujm*IK<',
			'Games':'123456'
}
import sys,pyperclip
if len(sys.argv) < 2:
	print('Usage: Python pw.py [account] -copy account password')
	sys.exit()
	
account = sys.argv[1]

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('password for' + account + 'copied to clipboard')
else:
	print('No account named ' + account)

'''批处理文件的使用'''
# cat pw.bat
'''

@py.exe C:\PATH\TO\pw.py %*
@pause
'''
# 放在C:\Windows目录下

# 实践项目
'''
编写一个名为 printTable()的函数，它接受字符串的列表的列表，将它显示在组织良好的表格中，每列右对齐。
假定所有内层列表都包含同样数目的字符串。例如，该值可能看起来像这样：
tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

你的 printTable()函数将打印出：

  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose

'''
# 我的答案
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
def printTable(aList):
    # colWidths=[]
    
    for i in range(0,len(aList[0])):
        #print(i)
        for j in range(0,len(aList)):
            #max=len(aList[i][j])
            print(aList[j][i].rjust(10),end=' ')
        print() # 换行


printTable(tableData)

'''
colWidth还不知道怎么用。
有看到一个比较好的答案:https://www.jianshu.com/p/62e79c9de352。
'''
"""下面是代码正文"""
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    # 下面是为了求每个内层列表的最长字符串的长度
    colWidths = [0] * len(tableData)
    for i in range(len(colWidths)):
        colWidths[i] = len(sorted(tableData[i], key=(lambda x: len(x)))[-1])
    
    for x in range(len(tableData[0])):
        for y in range(len(tableData)):
            print(tableData[y][x].rjust(colWidths[y]), end=' ')
        print('')    # 换行

printTable(tableData)






















