# 1859. 백만 장자 프로젝트

test_case = int(input())

for tc in range(1, test_case+1):
    answer = 0
    n = int(input())
    nums = list(map(int, input().split()))
    
    max_num = nums[-1]
    for num in nums[-1::-1]:
        if num > max_num:
            max_num = num
        else:
            answer += max_num - num
        
    print(f'#{tc} {answer}')