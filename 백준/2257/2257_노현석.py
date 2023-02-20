string = input()
stack = []
my_dict = {'H' : 1, 'C' : 12, 'O' : 16}

for c in string:
  if c == '(':
    stack.append(c)
  elif c == 'H' or c == 'C' or c == 'O':
    stack.append(my_dict[c])
  elif c == ')':
    temp = 0
    while True:
      if stack[-1] == '(':
        stack.pop()
        stack.append(temp)
        break
      else:
        temp += stack.pop()
  else:
    stack.append(stack.pop() * int(c))

print(sum(stack))