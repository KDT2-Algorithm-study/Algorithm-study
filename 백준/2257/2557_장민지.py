string = input()
alpa_dict = {"H":1, "C":12, "O":16} # 알파벳일 경우 딕셔너리로 숫자 출력해주기
stack = []

for s in string:
    if s == "(":
        stack.append(s)
        print(stack)

    elif s == ")": # 닫힌 괄호면 result = 0 만들어주고 반복문 돌기
        result = 0

        while True: # 스택 도는 while문 시작
            cur = stack.pop() # 끝값을 빼면서

            if cur == "(": # 끝값이 ( 면 While문 종료
                break
            else:
                result += cur    

        stack.append(result)

    elif s in alpa_dict:
        stack.append(alpa_dict[s])
        
    # 숫자면
    else:
        stack[-1] *= int(s)

print(sum(stack))