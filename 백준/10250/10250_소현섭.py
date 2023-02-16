for test_case in range(1, int(input())+1):
    h, w, n = map(int, input().split())
    print(((n-1)%h+1)*100 + (n-1)//h+1)