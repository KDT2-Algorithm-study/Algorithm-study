# 1233. 사칙연산 유효성 검사
        
# import sys
# sys.stdin = open("input.txt", "r")
TEST_CASE = 10

for tc in range(1, TEST_CASE+1):
    answer = 1
    tree = list()
    N = int(input())
    
    for idx in range(N):
        line = input().split()
        tree.append(line[1])
        
        if answer:
            if idx < N // 2 and line[1].isdigit():
                answer = 0
            elif idx >= N // 2 and not line[1].isdigit():
                answer = 0
    
    print(f'#{tc}', answer)