s = input()
zero = len([i for i in s.split('1') if i not in ''])
one = len([i for i in s.split('0') if i not in ''])
print(one) if zero >= one else print(zero)