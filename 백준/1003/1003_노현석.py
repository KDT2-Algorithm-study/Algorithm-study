'''
0, 1의 등장횟수도 피보나치 수열과 같이 나온다
'''

t = int(input())

for _ in range(t):

    n = int(input())
    zero = [1, 0, 1] # 0 등장 1, 0, 1, 1, 2, 3... 
    one = [0, 1, 1] # 1 등장 0, 1, 1, 2, 3, 5...

    if n >= 3:
        for i in range(3, n+1):
            # 피보나치 수열을 따라 n까지의 등장횟수 저장
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print(zero[n], one[n])