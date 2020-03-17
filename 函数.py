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


'''
异常处理
可能出错的语句放在try语句中，如果错误发生，程序执行就立即转到接下来的except子句开始处，不会执行try中剩下的语句。

'''
def spam(divideBy):
	try:
		return 42 / divideBy
	except ZeroDivisionError:
		print('Error:Invalid argument')
		
print(spam(2))
print(spam(0))
		
	
	


'''一个小程序'''
import random
secretNumber = random.randint(1,20)
print("Input number between 1-20")
# 猜6次
for guessesTaken in range(1,7):
	print("Take a guess")
	guess = int(input())
	if guess < secretNumber:
		print("You guess is too low")

	if guess > secretNumber:
		print("You guess is too high")
	else:
		break # 正确猜中
if guess == secretNumber:
	print("Good job, bingo.")
else:
	print("You did not guess right after 6 times")
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	






