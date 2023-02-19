# 2257 화학식량
num = {'H':1, 'C':12, 'O':16} # 각 원소의 값
lst = [] # 값을 쌓아줄 빈 리스트 생성
for i in input(): # 입력 문자열 순회
    if i == '(': # 열린 괄호는 닫힌 괄호를 만나면 열린 괄호까지의 값을 더해 주기 위해 
        lst.append(i) # 리스트에 쌓아준다.
    elif i ==')': # 닫힌 괄호를 만나면
        cnt = 0
        while 1:
            n = lst.pop() # 쌓여있는 값 뒤부터 
            if n == '(': # 열린 괄호를 만날 때 까지
                break
            else: # 하나씩 지우면서 값을 더해주고
                cnt += n
        lst.append(cnt) # 괄호 안의 값이 모두 더해지면 다시 리스트에 쌓아준다.
    elif i in num: # 만약 원소를 만나면
        lst.append(num[i]) # 원소의 값을 쌓아준다.
    else: # 원소도 아니고 괄호도 아니라면
        lst[-1] *= int(i) # 쌓여있는 값 중 가장 끝에 있는 값을 숫자 i만큼 곱해준다.
print(sum(lst)) # 쌓여있는 값들을 모두 합하여 출력.