T = int(input())

for t in range(T) :
    p, q, r, s, w = map(int, input().split())
    print(f"#{t+1} {min(p * w, q if w <= r else q + (w-r) * s)}")