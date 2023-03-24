def solution(numer1, denom1, numer2, denom2):
    N,M=[numer1*denom2+numer2*denom1,denom1*denom2]
    
    X = max(N,M)
    a = 0
    
    for num in range(X,0,-1):
        if N%num == 0 and M%num==0:
            a = num
            break
    answer = [N/a,M/a]
    
    return answer