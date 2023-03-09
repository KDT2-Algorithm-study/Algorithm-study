# 반복문으로 구현
def loop(n, m):
    output = 1
    for _ in range(1, m+1):
        output *= n
    return output

while True:
    try:
        t = int(input())
        n, m = map(int, input().split())
        print(f"#{t} {loop(n, m)}")
    except:
        break

# 재귀함수로 구현
# 수열의 점화식
# 이웃한 항의 관계를 통해 수열을 나타내는 것

def rcrs(n, m): # 3 2
    if m == 1: 
        return n 
    elif m >= 2:    # m이 2 이상의 수일 때 
        return n * rcrs(n, m-1)

while True:
    try:
        t = int(input())
        n, m = map(int, input().split())
        print(f"#{t} {rcrs(n, m)}")
    except:
        break
