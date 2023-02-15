from collections import deque

n, k = map(int, input().split())
yosepus = deque()
for i in range(n):
    yosepus.append(i+1)

print('<', end = '')
while len(yosepus) > 1: # 마지막 숫자 뒤에 '>'를 붙여주기 위해 하나 남겨둠
    yosepus.rotate(-k) # 맨 앞 숫자가 맨 뒤로 K번 이동
    print(yosepus.pop(), end = ', ')

print(f'{yosepus.pop()}>')