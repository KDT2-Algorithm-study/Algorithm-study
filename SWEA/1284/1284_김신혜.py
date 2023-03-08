def pq(p, q):
    if P > Q:
        return Q
    else:
        return P
ans = 0

T = int(input())
for t in range(1, T+1):
    P, Q, R, S, W = map(int,input().split())
    P *= W
    if W <= R:
        ans = pq(P, Q)
    else:
        Q += ((W-R) * S)
        ans = pq(P, Q)

    print(f"#{t} {ans}")
