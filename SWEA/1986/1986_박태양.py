for i in range(int(input())):
    a = int(input())
    if a%2 == 0:
        # a(a//2+1) -a//2 홀수합
        # a(a//2+1) 짝수합
        # result = a(a//2+1) -a//2 -a(a//2+1) 
        result = -a//2
    else:
        # (a+1)((a+1)//2+1) -(a+1)//2 홀수합
        # (a+1)((a+1)//2+1) -(a+1) 짝수합
        # result = (a+1)((a+1)//2+1) -(a+1)//2 - ((a+1)((a+1)//2+1) -(a+1))
        result = (a+1)//2
    
    print(f'#{i+1} {result}')
