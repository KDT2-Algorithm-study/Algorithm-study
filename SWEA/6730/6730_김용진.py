# 장애물 경주 난이도
# 풀고나서 제출이 안되서 보니까 오늘은 쉬는 날이네요 하하하하
# 일단 풀었으니 제출 하겠습니다.
# 주어진 테스트 케이스와 값은 동일하게 나오는데 나머지는 모르겠네요..
import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):
    a = []
    b = []
    num = int(input())
    block = list(map(int,input().split()))
    for i in range(1,num):
        if block[i-1] < block[i]:
            a.append(block[i]-block[i-1])
        elif block[i-1] > block[i]:
            b.append(block[i-1]-block[i])
        elif block[i-1] == block[i]:
            a.append(0)
            b.append(0)
        
    if len(a) == 0:
        a.append(0)
    elif len(b) == 0:
        b.append(0)
    print(f'#{t} {max(a)} {max(b)}')