s = input()
while '11'in s:
    s=s.replace('11','1')
while '00'in s:
    s=s.replace('00','0')
print(min(s.count('1'),s.count('0')))