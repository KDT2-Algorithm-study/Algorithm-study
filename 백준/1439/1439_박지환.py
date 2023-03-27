strs = input()
zero, one, before_num = 0, 0, '2'

for i in strs:
    if i != before_num:
        if i == '1':
            one += 1
        else:
            zero += 1
            
        before_num = i
        
print(min(zero, one))