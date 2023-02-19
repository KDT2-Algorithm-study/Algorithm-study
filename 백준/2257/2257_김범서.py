size = {'H': 1, 'C': 12, 'O': 16}

ipt = input()
stack = list()

# 입력받은 식을 읽는다
for element in ipt:
    # 여는 괄호일 때
    if element == '(':
        stack.append(element)
    # 닫는 괄호일 때
    # 여는 괄호가 나올 때까지 pop을 한다
    # 그 전까지 나오는 수를 더한 값을 여는 괄호가 나온 후 push한다
    elif element == ')':
        temp = 0
        while True:
            now = stack.pop()
            if now == '(':
                stack.append(temp)
                break
            else:
                temp += now
    # 숫자일 때
    # pop을 해 숫자를 곱한 값을 다시 push한다
    elif element.isdigit():
        temp = stack.pop()
        stack.append(temp * int(element))
    # H, C, O 중 하나일 때
    # 딕셔너리를 이용해 원자의 원자량을 더해준다
    else:
        stack.append(size[element])

print(sum(stack))
