a = int(input())
count = 0
for n in range(1,a+1):
    while True:
        if n%5==0:
            n/=5
            count +=1
        else:
            break
print(count)