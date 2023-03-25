# 120808. 분수의 덧셈

def solution(numer1, denom1, numer2, denom2):
    answer = []
    
    numer3 = numer1 * denom2 + numer2 * denom1
    denom3 = denom1 * denom2
    
    gcd = min(numer3, denom3)
    while True:
        if numer3 % gcd == 0 and denom3 % gcd == 0:
            break
        gcd -= 1
        
    answer.append(numer3 // gcd)
    answer.append(denom3 // gcd)
    
    return answer