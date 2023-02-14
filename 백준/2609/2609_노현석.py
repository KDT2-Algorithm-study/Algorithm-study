def gcd(x, y): # 유클리드 호제법을 이용한 최대공약수 구하는 함수
    if x % y == 0: 
        return y
    else: # 나머지가 존재하면 재귀적으로 호출
        return gcd(y, x % y)

a,b = map(int, input().split())
res1 = gcd(a, b) 
res2 = round((a * b) // res1) # a * b == 최대공약수 * 최소공배수
print(res1, res2, sep='\n')