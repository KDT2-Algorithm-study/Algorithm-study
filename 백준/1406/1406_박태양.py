import sys
input = sys.stdin.readline

st1 = list(input().rstrip())
st2 = []

for _ in range(int(input())):
	command = list(input().split())

	if command[0] == 'L':
		if st1:
			st2.append(st1.pop())
            
	elif command[0] == 'D':
		if st2:
			st1.append(st2.pop())

	elif command[0] == 'B':
		if st1:
			st1.pop()
            
	else:
		st1.append(command[1])
        
print(''.join(st1), end='')
print(''.join(reversed(st2)), end='')