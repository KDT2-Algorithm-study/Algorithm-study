# 뒤집기
# 처음에 deque를 사용했는대 시간초과로 인해 list로 다시 풀었습니다.
# 다른 분들의 코드를 보니까 너무 간단하네요 하하하
import sys
sys.stdin = open('input.txt','r')

num = list(input())
num1 = num[:] # num의 모든 요소를 복사한다고 하내요 처음 알았어요 ㅎㅎ
cnt0 = 0
cnt1 = 0

while 1:
    if num[0] == '1':
        num.append(num.pop(0))
    else:
        i = 1
        while 1:
            if num[0] == num[i]:
                num[i] = '1'
                i += 1
                if i == len(num):
                    break
            else:
                cnt1 += 1
                break
        num[0] = '1'
        num.append(num.pop(0)) # 비효율 적이다고 하셨던거 같은데 일단은 다른게 생각이 안나서 이렇게 풀었습니다.
    if len(num) == num.count('1'):
        break

while 1:
    if num1[0] == '0':
        num1.append(num1.pop(0))
    else:
        x = 1
        while 1:
            if num1[0] == num1[x]:
                num1[x] = '0'
                x += 1
                if x == len(num1):
                    break
            else:
                cnt0 += 1
                break
        num1[0] = '0'
        num1.append(num1.pop(0))
    if len(num1) == num1.count('0'): 
        break

print(min(cnt0,cnt1))


