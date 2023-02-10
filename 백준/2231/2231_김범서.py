n = int(input())

for i in range(1, n):        # 1부터 시험해보기
    total = i
    temp = i

    while temp:              # i의 각 자리수 더하기
        total += (temp % 10)
        temp = temp // 10
    
    if total == n:           # i의 각 자리수와 i를 더한 값이 n과 같으면
        print(i)             # i를 출력하고 루프에서 나온다.
        break
else:
    print(0)                 # 만족하는 수가 없는 경우 0을 출력한다.
