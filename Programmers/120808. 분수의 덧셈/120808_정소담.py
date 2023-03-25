def solution(numer1, denom1, numer2, denom2):
    answer = []
    numer = (numer1 * denom2) + (numer2 * denom1)
    denom = denom1 * denom2
    num = min(numer,denom)
    for i in range(num,1,-1):
        if numer % i == 0 and denom % i == 0:
            numer //= i
            denom //= i
    answer.append(numer)
    answer.append(denom)
    return answer