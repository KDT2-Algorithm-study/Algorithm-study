formula = input()
tmp = ''

cnt, cnt_max = 0, 0 # 괄호의 최대 개수 구하기, 괄호 안쪽부터 계산하기 위함
for j in formula:  
    if j == '(':
        cnt += 1
        if cnt_max < cnt:
            cnt_max = cnt
    elif j == ')':
        cnt -= 1

cnt = 0
for i in range(cnt_max, -1, -1): # 괄호 안쪽부터 차례대로 계산
    for j in range(len(formula)):
        if formula[j] == '(':
            cnt += 1
            tmp += formula[j]
        elif formula[j] == ')':
            cnt -= 1
            tmp += formula[j]
            
        elif cnt == i: 
            if formula[j].isnumeric(): # 숫자일 때 뒤로 돌아가면서 괄호를 찾음
                cnt_zero = 0
                for k in range(j-1, -1, -1):
                    if formula[k] == '(':
                        cnt_zero += 1
                    elif formula[k] == ')':
                        cnt_zero -= 1
                    
                    if cnt_zero == 0:
                        tmp += formula[k:j] * (int(formula[j]) -1)
                        break

            else:
                tmp += formula[j]
        
        else: 
            tmp += formula[j]

    formula = tmp
    tmp = ''

chemical_dict = {'H':0, 'C':0, 'O':0} # 원자 개수 구하기

for element in formula:
    if element in chemical_dict:
        chemical_dict[element] += 1

print( chemical_dict['H'] + chemical_dict['C']*12 + chemical_dict['O']*16)           



# # 1. 괄호 안을 먼저 계산하는 방법에 대해 생각

# # 2. 알파벳 개수를 세는 방법

# # chemical_dict = {'H':0, 'C':0, 'O':0}

# # for i in formula:
# #     if i in chemical_dict:
# #         chemical_dict[i] += 1

# # print(chemical_dict)