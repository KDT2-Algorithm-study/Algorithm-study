import math

def solution(numer1, denom1, numer2, denom2):
    de_gcd = math.gcd(denom1,denom2)
    numer3 = numer1*(denom2//de_gcd)+numer2*(denom1//de_gcd)
    denom3 = denom1*denom2//de_gcd
    g = math.gcd(numer3,denom3)
    answer = [numer3//g, denom3//g]
    return answer

n1, d1, n2, d2 = 9,2,1,3
print(solution(n1,d1,n2,d2))