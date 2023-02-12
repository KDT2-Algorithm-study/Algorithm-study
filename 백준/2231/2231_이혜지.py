a = int(input())
n= 1

for _ in range(1, 1000001) :
    # 정수 n을 N (li)에 넣는 리스트 컴프리헨션
    N = [int(i) for i in str(n)] 
    # print(N)
    summ = n + sum(N)
    # print(summ)
    if summ == a :
        print(n)
        break
    elif n == 1000000 :
        print(0)
    else :
        n += 1
  