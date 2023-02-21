# test.py
# 1, 2, 3, 4, 5, 6, 7 // 7(N)%3(K) == 1 // 1,K+1
#                        7//3 == 2
# 0, 1, 2, 4, 5, 7    // 6%3(K)
# 1, 4, 5
'''
<3, 6, 2, 7, 5, 1, 4>
'''
# [1, 2, 3, 4, 5, 6, 7] idx (2) remove
# [1, 2, 4, 5, 6, 7] idx(4) remove
## idx(2) idx(5)
# 6 0 1
# 5 + 3 % len(7)

# [1, 2, 4, 5, 7] 2: idx(1) remove
# [1, 4, 5, 7] 7: idx(3) remove
## idx(1) idx(4)
# 0 1 2
# [1, 4, 5] 5: idx(2) remove
## idx(2)
# 0 1 0
# [1, 4] 1: idx(0) remove
# [4] 4: idx(0) remove
## idx(0) idx(1)

# slst = sum(lst)
# t = 0
N, K = map(int,input(). split())
K2 = K

lst = [ i for i in range(1,int(N)+1)]
lst2 = []
a = []
idx = 0

'''
@comment
K의 값을 미리 1 빼둠
아래 코멘트 참조
'''
K -= 1
while True: 
    cnt = 0
    # print(f"K = {K}")
    # print(lst)

    '''
    @comment
    for k in lst[K-1::K2]은 매 루프마다 K를 계속 -1 해서 계산해야 하기 때문에
    K를 미리 1을 빼고 시작
    '''
    for k in lst[K::K2]:    
        a.append(k)
        cnt += 1

    idx2 = idx
    for mem in a[idx2:]:
        lst.remove(mem)
        idx += 1
        
    if not lst:
        break

    '''
    @comment
    K가 가르킬 다음 인덱스는 K위치를 포함해 K2번째, 즉 K + K2 - 1인데
    K2를 더하는 것과 1을 빼는 것이 cnt만큼 반복되므로 (K2-1) * cnt
    '''
    K = (K + (K2-1) * cnt) % len(lst)
    
# 출력 형식 문제 출력에 맞게 조정!
print('<', end = '')
print(*a, sep = ', ', end = '')
print('>', end = '')