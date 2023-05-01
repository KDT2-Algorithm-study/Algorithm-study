import sys
from collections import deque
input = sys.stdin.readline

front_word = deque(list(input().rstrip()))
back_word = deque()

n = int(input())

for _ in range(n):
    command = input().rstrip()

    if command == 'L':
        if front_word:
            back_word.appendleft(front_word.pop())
    elif command == 'D':
        if back_word:
            front_word.append(back_word.popleft())
    elif command == 'B':
        if front_word:
            front_word.pop()
    elif 'P' in command:
        front_word.append(command[2])    
    
print(''.join(front_word)+''.join(back_word))

# ======================================================

# 시간 초과

# import sys
# input = sys.stdin.readline

# sentence = input().rstrip()
# n = int(input())
# cursor = len(sentence)

# letter_list = [] 
# for letter in sentence:
#     letter_list.append(letter)

# for _ in range(n):
#     command_list = input().split()
#     if command_list[0] == 'L':
#         if cursor != 0:
#             cursor -= 1
    
#     elif command_list[0] == 'D':
#         if cursor != len(letter_list):
#             cursor += 1
    
#     elif command_list[0] == 'B':
#         if cursor != 0:
#             letter_list.pop(cursor-1)
#             cursor -= 1
            
#     elif command_list[0] == 'P':
#         letter_list.insert(cursor, command_list[1])
#         cursor += 1
            

# print(''.join(letter_list))