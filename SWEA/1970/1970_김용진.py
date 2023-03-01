# 쉬운 거스름돈
import sys
sys.stdin = open('input.txt','r')

T = int(input())
a = [50000,10000,5000,1000,500,100,50,10]
for t in range(1,T+1):
    N = int(input())
    b = []
    for i in a:
        
        if N>=i:
            c = N//i
            N = N%i
            b.append(c)
        else:
            b.append(0)
    print(f"#{t}")
    print(*b)


# 쪽팔린 노가다 코드........... 풀고나서 아닌거 같아서 다시 풀었습니다.....

# T = int(input())

# for t in range(1,T+1):
#     a = []
#     N = int(input())
#     if N >= 50000:
#         b = N//50000
#         N = N % 50000
#         a.append(b)
#     else:
#         a.append(0)
#     if 50000>N>=10000:
#         b = N//10000
#         N = N% 10000
#         a.append(b)
#     else:
#         a.append(0)
#     if 10000>N>=5000:
#         b = N//5000
#         N = N%5000
#         a.append(b)
#     else:
#         a.append(0)
#     if 5000>N>=1000:
#         b = N//1000
#         N = N%1000
#         a.append(b)
#     else:
#         a.append(0)
#     if 1000>N>=500:
#         b = N//500
#         N = N%500
#         a.append(b)
#     else:
#         a.append(0)
#     if 500>N>=100:
#         b = N//100
#         N = N%100
#         a.append(b)
#     else:
#         a.append(0)
#     if 100>N>=50:
#         b = N//50
#         N = N%50
#         a.append(b)
#     else:
#         a.append(0)
#     if 50>N>=10:
#         b = N//10
#         N = N%10
#         a.append(b)
#     else:
#         a.append(0)

#     print(f"#{t}")
#     print(*a)