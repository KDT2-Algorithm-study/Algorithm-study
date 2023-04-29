# 2579. 계단 오르기

import sys
input = sys.stdin.readline


N = int(input())
stairs = [int(input()) for _ in range(N)]

MAX_STAIRS = 300
stairs += [0, 0]    # 점화식 연산을 위한 필요 최소 stair 충족
acc = [0] * MAX_STAIRS
acc[0] = stairs[0]
acc[1] = stairs[0] + stairs[1]
acc[2] = max(stairs[0], stairs[1]) + stairs[2]

for i in range(3, N):
    acc[i] = max(acc[i-2], acc[i-3]+stairs[i-1]) + stairs[i]

answer = acc[N-1]
print(answer)