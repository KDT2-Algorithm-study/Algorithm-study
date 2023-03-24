def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def solution(numer1, denom1, numer2, denom2):
    num = numer1 * denom2 + numer2 * denom1
    deno = denom1 * denom2

    gcdd = gcd(num, deno)
    
    answer = [num//gcdd, deno//gcdd]
    return answer


numer1, denom1, numer2, denom2 = map(int, input().split())

print(solution(numer1, denom1, numer2, denom2))