# 처음 제출한 풀이
for _ in range(10):
    t = int(input())
    n,m = map(int,input().split())
    print(f'#{t}',n**m)

# 재귀 연습해보는 주간이라서 재귀를 사용해서도 풀었습니다
def power(n,m):
    global num
    if m < 2:
        return num
    else:
        num *= n
        return(power(n,m-1))

for _ in range(10):
    t = int(input())
    n,m = map(int,input().split())
    num = n
    print(f'#{t}',power(n,m))