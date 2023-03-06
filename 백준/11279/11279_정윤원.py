import sys
input = sys.stdin.readline
import heapq

list1 = []
N = int(input())

for n in range(N) :
    number = int(input())
    if number : heapq.heappush(list1, number * -1)
    else :
        if list1 : print(heapq.heappop(list1) * -1)
        else : print(0)