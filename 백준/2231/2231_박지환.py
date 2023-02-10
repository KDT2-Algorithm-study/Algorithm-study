N = int(input())

if N <= 100: # 풀이 시간을 줄이기 위해서 100을 기준으로 나누었음
             # 각 자리 숫자의 합이 아무리 커도 100을 넘지않으므로
    for num in range(1, N + 1): # 1부터 N까지 반복
        cnt = 0
        for i in str(num): # 각 자리 숫자를 cnt에 더함
            cnt += int(i)

        if num + cnt == N: # num이 생성자인지 판단
            print(num)
            break

        elif num == N: # 생성자가 없는 경우 0을 출력
            print(0)

else:
    for num in range(N - 100, N + 1):  # N - 100부터 N까지 반복
        cnt = 0
        for i in str(num):
            cnt += int(i)
        
        if num + cnt == N: # num이 생성자인지 판단
            print(num)
            break

        elif num == N: # 생성자가 없는 경우 0을 출력
            print(0)