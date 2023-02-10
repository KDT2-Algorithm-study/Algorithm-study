# 분해합

import sys
sys.stdin = open('input.txt','r')

num = int(input()) # 입력 값
for i in range(num): # 0부터 num-1 까지
    b= list(map(int,str(i))) # b 리스트에 문자열로 받아 정수로 저장
    if sum(b) + i == num: # sum(b) => 각각의 숫자를 더한 값, i => 0부터 num-1 까지 증가하는 수 에서 입력값 num과 같다면
        break # for문 break 
print(i) # sum(b) = 18, i = 198 일때 입력 값 216을 만족하므로 출력은 i = 198