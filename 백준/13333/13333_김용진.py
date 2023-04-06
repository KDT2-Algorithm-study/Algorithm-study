# Q-인덱스
import sys
sys.stdin = open('input.txt','r')

T = int(input())
num = sorted(list(map(int,input().split())))

for i in range(T, -1 , -1):
    if i <= num[-i]:
        print(i)
        break