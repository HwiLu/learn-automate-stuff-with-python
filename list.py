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
for i  in range(list)


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
