def hanoi(n, s, e):     # n 원판을 s 에서 e 로 옮김
    if n == 1:
        print(s, e)
        return
    hanoi(n-1, s, 6-s-e)    # 1+2+3 == 6, 1->3, 6-1-3 == 2
    print(s, e)
    hanoi(n-1, 6-s-e, e)
    
n = int(input())
print(2**n-1)   # 1 + 2 + 4 + 8 + ...
hanoi(n, 1, 3)

# (4) 313   -  (2) 212     -  (1) 113     return
#                          -  (3) 132     return
#           -  (6) 223     -  (5) 121     return
#                          -  (7) 113     return