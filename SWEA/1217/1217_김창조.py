# 1217. 거듭 제곱

TEST_CASE = 10

def pow_recursion(b: int, p: int):
    if p == 1:
        return b
    
    return pow_recursion(b, p-1) * b

for _ in range(TEST_CASE):
    t = int(input())
    base, power = map(int, input().split())
    
    print(f"#{t} {pow_recursion(base, power)}")