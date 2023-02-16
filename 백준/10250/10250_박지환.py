T = int(input())
for _ in range(T):
    h, w, n = map(int, input().split())
    print(max((((n-1) % h)+1)*100, (n % h)*100) + ((n-1) // h) + 1)