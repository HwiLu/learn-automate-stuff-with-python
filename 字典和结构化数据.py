'''
键值对形式
myCat = {'size':'fat','color':'gray','disposition':'loud'}

字典的表项是不排序的。
'''

# 字典的方法
key() # 打印键
value() # 打印值
items() # 打印元素

# 检查字典是否存在键或者值

in 

not in

# get()方法
'''
有两个参数：要取得其值的键，如果该键不存在时，返回的备用值。
'''

# setdefault()
'''用法
setdefault(key,value)
传递给该方法的第一个参数是要检查的键，第二个参数，是如果该键不存在时要设置的值，如果该键存在，方法就会返回该键原有的值。

'''
# 计算一个字符在字符串里出现的次数
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {} # 定义一个空字典
for character in message: # 遍历message中所有的字符
    count.setdefault(character, 0) # 如果字符在 count 里不存在，则将该字符在字典里的值设置为0
    count[character] = count[character] + 1 # 存在的键其值会自动 +1 
print(count)


# 漂亮打印

# pprint 包
import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {} # 定义一个空字典
for character in message: # 遍历message中所有的字符
    count.setdefault(character, 0) # 如果字符在 count 里不存在，则将该字符在字典里的值设置为0
    count[character] = count[character] + 1 # 存在的键其值会自动 +1 
pprint.pprint(count)

# 将漂亮地打印成以下格式
'''
{' ': 13,
 ',': 1,
 '.': 1,
 'A': 1,
 'I': 1,
 'a': 4,
 'b': 1,
 'c': 3,
 'd': 3,
 'e': 5,
 'g': 2,
 'h': 3,
 'i': 6,
 'k': 2,
 'l': 3,
 'n': 4,
 'o': 2,
 'p': 1,
 'r': 5,
 's': 3,
 't': 6,
 'w': 2,
 'y': 1}
 '''

 # 如果无需将输出结果打印在屏幕上，可以使用pprint.pformat()函数。


 # 可以使用字典的数据结构完成井字棋盘的建模
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M':
' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?') 
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)

# 字典和列表嵌套

''' 字典适合有序的值，字典适用于包含关联的键和值。 '''

# 实现项目
## 物品清单
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL THIS PART IN
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))

displayInventory(stuff)


# 5.6.2 列表到字典的函数
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL THIS PART IN
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))


def addToInventory(inventory,addedItems):
    for key in addedItems:
        inventory.setdefault(key, 0)
        inventory[key] += 1
    return inventory
inv = {'gold coin':42, 'rope':1}
# list
dragonLoot = ['gold coin','dagger','gold coin','gold coin','ruby']

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)