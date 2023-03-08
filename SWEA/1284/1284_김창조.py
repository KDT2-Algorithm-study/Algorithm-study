# 1284. 수도 요금 경쟁

test_case = int(input())

for T in range(1, test_case+1):
    answer = 0
    
    p, q, r, s, w = map(int, input().split())
    
    a_charge = p * w
    b_charge = q if w <= r else (q + s*(w-r))
    
    answer = min(a_charge, b_charge)
    
    print(f"#{T} {answer}")