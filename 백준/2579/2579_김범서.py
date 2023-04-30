import sys
input = sys.stdin.readline

n = int(input())
stair = [0 for i in range(n)]
score = [0 for i in range(n)]

for i in range(n):
	score[i] = int(input())

if len(score) < 3:
	print(sum(score))
else:
	stair[0] = score[0]
	stair[1] = max(score[0] + score[1], score[1])

	for i in range(2, n):
		stair[i] = max(stair[i - 3] + score[i - 1] + score[i], \
		stair[i - 2] + score[i])
	
	print(stair[-1])
