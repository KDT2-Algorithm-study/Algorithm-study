n = input()
x = [i for i in n.split('0') if len(i)>0]
y = [i for i in n.split('1') if len(i)>0]
print(min(len(x),len(y)))