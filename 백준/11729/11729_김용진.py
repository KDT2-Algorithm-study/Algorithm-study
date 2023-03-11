# 하노이 탑 이동 순서
# 답을 보고 튜터로 동작을 봐도 동작이 왜 이렇게 이루어지는지 모르겠네요...

import sys
sys.stdin = open('input.txt','r')

num = int(input())

def hanoi(num, one , two ,three): 
    if num == 0: 
        return
    hanoi(num-1, one, three, two)
    print(one,two)
    hanoi(num-1, three, two, one) 

    

print(2**num -1)
hanoi(num,1,3,2)