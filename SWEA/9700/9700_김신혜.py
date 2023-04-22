
import sys
T = int(input())
i = 0
for t in range(1,T+1):
    p, q = map(float, input().split())
    
    # 가장 처음 시도에서 뒤집혀서 실패할 확률 (1 - p)
    # 1번 뒤집은 다음 시도에서 올바른 면으로 성공할 확률 q
    s1 = (1 - p) * q
    
    # 가장 처음 시도에서 올바른 면으로 성공할 확률 p
    # 1번 뒤집은 다음 시도에서 뒤집혀서 실패할 확률 (1 - q)
    # 2번 뒤집은 다음 시도에서 올바른 면으로 성공할 확률 q
    s2 = p * (1 - q) * q
    
    '''s1 < s2 이면 “YES”를 아니면 “NO”를 출력한다.'''
    if s1 < s2:
        ans = 'YES'
    else: 
        ans = 'NO'
    print(f'#{t} {ans}')
