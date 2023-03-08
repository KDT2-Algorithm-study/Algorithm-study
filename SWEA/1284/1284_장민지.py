T = int(input())

for t in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    # A사
    a = P * W
    # B사
    if W > R:
        b = Q + ((W - R) * S)
    else:
        b = Q
    result = min(a, b)
    print(f"#{t} {result}")