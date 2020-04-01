'''
if else
'''
if name == 'Mary':
    print ('Hello Mary')
    if 表达式
        动作
    else:
        动作
        

if 条件:
    动作
    elif 条件:
        动作
    elif expression:
        pass

while 条件:
    动作


break
'''
退出循环
'''

continue
'''
退出本次循环，开始开一次循环
'''
'''
for range()
'''
for i in range(5):
    pass


'''range()开始、停止和步长'''
for i in range(0,20,2):

'''导入模块'''
import random
for i in range(5):
    print(random.randint(1,10))

'''sys.exit()提前结束程序'''
import sys
while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')

