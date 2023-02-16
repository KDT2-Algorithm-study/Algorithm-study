'''
word = input()
cnt = 0
list1 = ['']

for i in range(len(word)) :
    if word[i] == '(' : 
        cnt += 1 
        list1.append('')

    elif word[i] == ')' : 
        if i+1 < len(word) and ord('1') <= ord(word[i+1]) <= ord('9') : # 숫자면
            list1[cnt] *= int(word[i+1])
        cnt -= 1
        list1[cnt] += list1.pop()

    elif word[i] in ['H', 'C', 'O'] : 
        if  i+1 < len(word) and ord('1') <= ord(word[i+1]) <= ord('9') :
            list1[cnt] += word[i] * int(word[i+1])
        else :
            list1[cnt] += word[i]

print(list1[0].count('H') + list1[0].count('C') * 12 + list1[0].count('O') * 16)
'''

# 230216 10:49 수정 '2257_정윤원_2'

word = input()
cnt = 0
list1 = ['']

for i in range(len(word)) :
    if word[i] == '(' : 
        cnt += 1 
        list1.append('')

    elif word[i] == ')' : 
        if i+1 < len(word) and word[i+1].isdigit() : # 숫자면
            list1[cnt] *= int(word[i+1])
        cnt -= 1
        list1[cnt] += list1.pop()

    elif word[i] in ['H', 'C', 'O'] : 
        if  i+1 < len(word) and word[i+1].isdigit() :
            list1[cnt] += word[i] * int(word[i+1])
        else :
            list1[cnt] += word[i]

print(list1[0].count('H') + list1[0].count('C') * 12 + list1[0].count('O') * 16)