# 유클리드 호제법
# 두 수의 최대공약수를 구할 수 있다.
def get_gcd(n1, n2):
    while True:
        if not (n1 % n2):
            return n2
        n1, n2 = n2, n1 % n2

number = list(map(int, input().split()))
large = max(number)
small = min(number)
gcd = get_gcd(large, small)

print(gcd)
print(large * small // gcd)
