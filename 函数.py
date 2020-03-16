import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is wrong'

answer=random.randint(1,9)
result=getAnswer(answer)
print(result)

'''
上述代码可能会输出None。
表示没有值，None是NoneType数据类型的唯一值
'''

'''关键字参数和print()'''
'''
有些函数有可选的关键字参数，如print、random.randint等。
关键字参数通常用于可选变元，print()的可选变元有end和sep。

'''

print('Lucy','Kafka','Mike')

print('Lucy','Kafka','Mike',end='.',sep=',')