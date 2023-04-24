for t in range(1, int(input()) + 1):
    p, q = map(float, input().split())
    one = ((1 - p) * q)
    two = (p * (1 - q) * q)
    if one < two:
        print(f"#{t} YES")
    else:
        print(f"#{t} NO")