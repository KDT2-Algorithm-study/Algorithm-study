n = int(input())
q_index = map(int, input().split())

q_index = sorted(q_index)

for i in range(n+1):
    if q_index[-i] >= i:
        if i == n:
            print(i)
            break
        
        elif i >= q_index[n - i - 1]:
            print(i)
            break