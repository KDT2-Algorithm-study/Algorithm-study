n = int(input())
papers = sorted(list(map(int, input().split())), reverse=True)

for i in range(n):
    if papers[i] <= i:
        print(i)
        break
else:
    print(n)
