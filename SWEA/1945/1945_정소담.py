num = [2, 3, 5, 7, 11]

def divide(n):

    if n == 1:
        print(f'#{t}', *cnt)
        return
    
    for i in range(5):
        if n % num[i] == 0:
            cnt[i] += 1
            n //= num[i]
    divide(n)

for t in range(1,int(input())+1):
    cnt = [0, 0, 0, 0, 0]
    n = int(input())
    divide(n)