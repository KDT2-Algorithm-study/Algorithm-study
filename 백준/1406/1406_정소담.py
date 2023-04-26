import sys
input = sys.stdin.readline

word = list(input().strip())
word2 = []

for _ in range(int(input())):
    order = input().strip()
    if order == 'L':
        if len(word) == 0:
            continue
        word2.append(word.pop())
    elif order == 'D':
        if len(word2) == 0:
            continue
        word.append(word2.pop())
    elif order == 'B':
        if len(word) == 0:
            continue
        word.pop()
    elif order[0] == 'P':
            word.append(order[2])
word.extend(word2[::-1])
print(''.join(word))