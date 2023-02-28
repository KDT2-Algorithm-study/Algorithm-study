# 1970. 쉬운 거스름돈

change_lst = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

test_case = int(input())
for T in range(1, test_case+1):
    money = int(input())
    
    change_cnt_lst = [0, 0, 0, 0, 0, 0, 0, 0]    
    for idx, change in enumerate(change_lst):
        if money >= change:
            change_cnt_lst[idx] = money // change
        money %= change
    
    print(f"#{T}")
    print(*change_cnt_lst)