def get_gcd(n1, n2):
    while True:
        if not (n1 % n2):
            return n2
        n1, n2 = n2, n1 % n2

def solution(numer1, denom1, numer2, denom2):
    answer = [numer1 * denom2 + numer2 * denom1, denom1 * denom2]
    gcd = get_gcd(max(answer), min(answer))
    answer[0] //= gcd
    answer[1] //= gcd

    return answer
