# 1439. 뒤집기

word = input()

sequential_lst = [0, 0]
temp = 'a'
for i in range(len(word)):
    if temp != '0' and temp != '1':
        temp = word[i]
        sequential_lst[int(word[i])] += 1
    elif word[i] != temp:
        temp = word[i]
        sequential_lst[int(word[i])] += 1
    else:
        pass

print(min(sequential_lst))