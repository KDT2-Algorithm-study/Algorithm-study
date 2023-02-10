n = int(input())
for i in range(n+2): # 입력한 수 보다 1큰수 까지 순회
    m = list(str(i)) # i 각 자리수의 수 리스트
    num = i + sum(map(int,m)) # i + sum(자리수의 수) 
    if i > n: # 순회를 도는데 i가 입력한 수 보다 커지면 생성자가 없는 것으로
        print(0) # 0 출력
    else:
        if n == num: # 입력한 수와 i + sum(자리수의 수) 의 수가 같으면
            print(i) # 입력한 수의 가장 작은 생성자 임으로 출력하고 break
            break
# 0부터 1씩 커지는 수를 완전 탐색 해보았습니다.