# 1003 피보나치 함수
T = int(input())
for _ in range(T):
    num = int(input())
    zero = [1, 0] 
    one = [0, 1]
    # 규칙: 리스트[n-2] + 리스트[n-1] = 리스트[n]
    for _ in range(num): 
        zero.append(zero[-2] + zero[-1])
        one.append(one[-2] + one[-1])
    print(zero[num], one[num])