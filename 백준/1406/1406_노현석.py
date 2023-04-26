import sys
input = sys.stdin.readline

word = list(input().strip())
right = []
for _ in range(int(input())):
    now = list(input().split())
    if len(now) == 2:
        a, b = now
    else:
        a = now[0]
    
    if a == 'L' and len(word) != 0:
        right.append(word.pop())
    elif a == 'D' and len(right) != 0:
        word.append(right.pop())
    elif a == 'B' and len(word) != 0:
        word.pop()
    elif a == 'P':
        word.append(b)
right = right[::-1]
print("".join(word + right))