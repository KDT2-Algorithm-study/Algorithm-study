import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())
people = deque([i for i in range(1,n+1)])
person = []

while people:
    people.rotate(-(k-1)) # k 보다 1 작은 수 만큼 뒤로 보냄
    person.append(people.popleft()) # k번째 수 pop해서 새로운 리스트에 쌓기
print(f'<{", ".join(map(str,person))}>')