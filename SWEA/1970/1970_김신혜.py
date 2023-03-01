import sys
sys.stdin = open("ip.txt", "r")
cash = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

def money(C):
    lst = []
    for c in cash:
        if C//c == 1:
            lst.append(1)
        elif C//c > 1:
            lst.append(C//c)
        else:
            lst.append(0)
        C = C % c
    return lst

T = int(input())
for test_case in range(1, T + 1):
    changes = int(input())
    print(f'#{test_case}')
    print(*money(changes))