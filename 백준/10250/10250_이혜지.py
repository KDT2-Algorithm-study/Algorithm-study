T = int(input())

for _ in range(T) :
    h, w, n = map(int, input().split())
    f = n % h
    a = (n // h) + 1

    if f == 0 :
        f = h
        a = n // h   

    print(f, (2-len(str(a)))*'0', a, sep='')    