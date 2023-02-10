N = input()

N_int = int(N)

N_before = N_int - len(N) * 9 # 분해합이 되기 전의 최소 숫자
if N_before < 1 : N_before = 1

for i in range(N_before, N_int) :
    sum = i
    for j in str(i) :
        sum += int(j)
    
    if sum == N_int :
        print(i)
        break

else : print(0)