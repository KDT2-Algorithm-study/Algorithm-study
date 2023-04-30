from collections import deque
import sys
input = sys.stdin.readline

stack1 = deque(input().rstrip())
stack2 = deque()
n = int(input())

for i in range(n):
	command = list(input().split())
	if command[0] == 'P':
		stack1.append(command[1])
	elif command[0] == 'L':
		if stack1:
			stack2.appendleft(stack1.pop())
	elif command[0] == 'D':
		if stack2:
			stack1.append(stack2.popleft())
	else:
		if stack1:
			stack1.pop()

print(*stack1, *stack2, sep='')
