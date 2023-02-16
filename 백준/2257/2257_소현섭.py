n = input()
stack = []
hco_dict = {'H':1, 'C':12, 'O':16}

for x in n:
    if x == '(':
        stack.append(x)
    elif x == 'H' or x == 'C' or x == 'O':
        stack.append(hco_dict[x])
    elif x == ')':
        temp = 0
        while True:
            if stack[-1] == '(':
                stack.pop()
                stack.append(temp)
                break
            else:
                temp += stack.pop()
    else:
        stack.append(stack.pop()*int(x))

print(sum(stack))