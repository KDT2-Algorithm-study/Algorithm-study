# 재귀함수가 뭔가요?

import sys
sys.stdin = open('input.txt','r')

num = int(input())

student = "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다."
a = '"재귀함수가 뭔가요?"'
b = '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
c = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지."
d = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
e = '"재귀함수는 자기 자신을 호출하는 함수라네"'
f = "라고 답변하였지."

def question(i):
    global a,b,c,d,e,f
    if i == 0:
        print(('____' * (num-i)) + a)
        print(('____' * (num-i)) + e)
        print(('____' * (num-i)) + f)
        return 
    else:       
        print(('____' * (num-i)) + a)
        print(('____' * (num-i)) + b)
        print(('____' * (num-i)) + c)
        print(('____' * (num-i)) + d)
        question(i-1)
    print(('____' * (num-i)) + f)

print(student)
question(num)
            