'''列表'''

spam = ['cat','dog','rat']
'''以,分割'''

'''取值ֵ'''
spam[0]
spam[int(1.0)]

'''列表的元素可以为列表，类似有二维数组'''

spam = [['cat','bat'],[12,20]]
'''取值'''

spam[1][2]

'''负数下标'''
spam[-1] '''倒数第一个元素'''

'''切片'''
spam[0:2] '''取第1个到第3个元素值'''

len(spam)

spam[1] = 'manky'

list3 = list1 + list2

del spam[2]

''''''

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]  # 列表拼接
print('The cat names are:')
for name in catNames:
    print('  ' + name)

'''列表连接和复制'''

[1,2,3] + [a,b,c]

spam = [1,2,3]
spam * 3

# 列表循环
for i  in range(list):


# in 和not in
# 判断元素是否在列表中
if 'Tom' not in ['Lucy','Fancy','Kafre']:
    print(True)
else:
    print(False)

'''列表中的方法'''
index()
append()
insert()
remove()
sort()

'''字符串可以认为是单个文本字符的列表'''
name = 'Zophie'
name[0]
'''可变数据类型和不可变数据类型'''
'''
字符串是不可变数据类型
我们无法对字符串中的一个字符重新赋值，将导致TypeError错误.

只是我们可以改变一个字符串。使用切片和连接的方式

'''
>>> name = 'Zophie a cat'
>>> newName = name[0:7] + 'the' + name[8:12]
>>> name
'Zophie a cat'
>>> newName
'Zophie the cat'


# 元组
'''元组是列表数据类型的不可变形式'''

eggs = ('Hello','42','0.5')
eggs[0]
'''元组不能让他们的值修改、添加或删除'''

'''如果元组只有一个值，最后的,号告诉python这是个元组'''
>>> type(('hello',))
<class 'tuple'>
>>> type(('hello'))
<class 'str'>

# 类型转换
'''
可用list()和tuple函数进行相应的类型转换
'''


# 引用

'''
列表的赋值只是将列表的引用赋给了变量。 对于可变数据类型的值，例如列表和字典，
Python的变量只会保持其引用，对于不可变数据类型，比如字符串、整型和元组，Python变量就保存其本身。
'''
# 传递引用

#copy模块
'''
如果需要对一个变量中的列表修改，同时不修改原来的列表，就可以用copy()和deepcopy()函数。deepcopy()函数将
同时复制他们内部的列表。

'''

# 实践项目

# 4.10.1 逗号代码
def list2str(alist):
    print(alist)
    a = alist.pop()
    a = 'and  ' + a
    alist.append(a)
    b = ', '.join(alist)
    print(b)
    return(b)    # print改成return就可以返回结果

a = ['cat', 'dog', 'cow']
list2str(a)

'''
思路
先把列表最后一个
元素pop出来，并与and进行相加，再使用join方法将其拼接
''' 

# 字符图网络

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
print(len(grid))        # y
print(len(grid[0]))     # x
for x in range(0,len(grid[0])):
    for y in range(0,len(grid)):
        print(grid[y][x],end='')
    print('')

# 思路
'''
    使用递归循环获取二维列表元素值。
    可以使用len(grid)和len(grid[0])获取二维数组纵向和横向长度。
'''










