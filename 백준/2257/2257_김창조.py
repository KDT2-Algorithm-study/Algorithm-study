# 2257. 화학식량

import sys


chem_dict = {
    "H": 1,
    "C": 12,
    "O": 16
}

chem_word = sys.stdin.readline().rstrip()

stack = [0]
idx = 0
len_ = len(chem_word)
pop_num = 0

for idx in range(len_):
    word = chem_word[idx]
    
    if word == "(":
        stack.append(0)
        
    elif word == ")":
        if len(stack) <= 1:
            sys.exit("Wrong Input")
        pop_num = stack.pop()
        stack[-1] += pop_num
            
    elif word in "CHO":
        stack[-1] += chem_dict[word]
        
    elif word in "23456789":
        if chem_word[idx - 1] == ")":
            stack[-1] += pop_num * (int(word) - 1)
            
        elif chem_word[idx - 1] in "CHO":
            stack[-1] += chem_dict[chem_word[idx - 1]] * (int(word) - 1)
        
    else:
        sys.exit("Wrong Input")

print(stack[0])