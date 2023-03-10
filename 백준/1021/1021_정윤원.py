'''
import sys
sys.stdin = open('test.txt', 'r')
import sys
input = sys.stdin.readline
'''
from collections import deque
N, M = map(int, input().split())
list1 = deque(range(1,N+1))
list2 = list(map(int, input().split()))
list2.reverse()

cnt = 0
while list2 :
    number = list2.pop()
    indx = list1.index(number)

    if len(list1) >= indx * 2 : # len(list1) - indx >= indx : #-> 3번하고 1번 cnt++
        for i in range(indx) :
            list1.append(list1.popleft())
        cnt += indx

    else :  #-> 2번하고 1번cnt++
        for i in range(len(list1) - indx) :
            list1.appendleft(list1.pop())
        cnt += len(list1) - indx

    list1.popleft()

print(cnt)