d = {'H':1,'C':12,'O':16}
s = input()
stack = []
for i in s:
    if i.isdigit():
        stack.append(stack.pop()*int(i))
    elif i == '(':
        stack.append(i)
    elif i == ')':
        t = 0
        while True:
            k = stack.pop()
            if k == '(':
                stack.append(t)
                break
            else:
                t +=k
    else:
        stack.append(d[i])

print(sum(stack))