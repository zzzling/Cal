#coding:utf-8

import random
import csv
import time


while(True):
	str_input=input("你要做10，20，100，1000以内的加减法吗？请输入范围\n")
	try:
		rang = int(str_input)
		if(rang < 10 or rang > 1000):
			print("输入错误。请重新输入\n")
		else:
			break
	except:
		print("输入错误。请重新输入\n")
	
	

while(True):
	str_input = input("请问要做多少题？请输入数字\n")
	try:
		num = int(str_input)
		if(num < 10 or num > 1000):
			print("输入错误。请输入10到1000的数字。重新输入\n")
		else:
			break
	except:
		print("输入错误。请重新输入\n")

EachScore = 100/num
Score = 0
TotalTime = 0
WrongQuestion = []

print("---------------------开始做题-------------------")
for i in range(1,num+1):
	x = random.randint(1,rang)
	y = random.randint(1,rang)
	operator = random.randint(1,2)
	if(operator == 2 and x < y):
		temp = x
		x = y
		y = temp
	if(operator == 1):
		op_str = "+"
		result = x + y
	else:
		op_str = "-"
		result = x - y
	
	question = "第%d题： %d %s %d = " %(i,x,op_str,y)
	print(question)
	CurrentTime = time.time()
	str_input = input("请输入答案\n")
	try:
		input_result = int(str_input)
		if(input_result != result):
			RightOrWrong = False
			WrongQuestion.append(question)
		else:
			RightOrWrong = True
			Score += EachScore
	except:
			input_result = str_input
			RightOrWrong = False
			WrongQuestion.append(question)


	TimeSpan = time.time() - CurrentTime 
	TotalTime += TimeSpan


	with open('result.csv', 'a+',newline='') as csvfile:
		spamwriter = csv.writer(csvfile,dialect='excel')
		spamwriter.writerow([question , str_input,RightOrWrong,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), TimeSpan])


print("-------------------结果---------------------")
print("得分为 %d " %Score)
print("共耗时 %d秒 " %TotalTime)
print("--------------------------------------------")
print("错误题目")
for question in WrongQuestion:
	print(question)