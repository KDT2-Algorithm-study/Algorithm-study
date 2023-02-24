'''
import sys
sys.stdin = open('test.txt', 'r')
import sys
input = sys.stdin.readline
'''
from collections import deque

N = int(input())
list1 = list(range(N, 0, -1)) # 현재 카드 상태
list2 = list(map(int, input().split())) # 과정
result = deque()

for i in range(N) :
    repl =list2.pop()

    if repl == 1 :
        result.appendleft(list1.pop())
    elif repl == 2 :
        temp = result.popleft()
        result.appendleft(list1.pop())
        result.appendleft(temp)
    else : # repl == 3 
        result.append(list1.pop())

print(*result)