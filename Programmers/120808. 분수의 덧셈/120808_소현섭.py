def gcd(x, y):
    while y:
        x, y = y, x%y
    return x

def solution(numer1, denom1, numer2, denom2):
    numer, denom = numer1*denom2 + numer2*denom1, denom1*denom2
    gcd_num = gcd(numer, denom)
    return [numer//gcd_num, denom//gcd_num]