N = int(input())

stair = [0]*301

for i in range(N):
    stair[i]=int(input())

DP = [0]*301
DP[0] = stair[0]
DP[1] = stair[0]+stair[1]
DP[2] = max(stair[0]+stair[2], stair[1]+stair[2])

for i in range(3, N):
    DP[i] = max(DP[i-3] + stair[i-1] + stair[i], DP[i-2]+stair[i])

print(DP[N-1])