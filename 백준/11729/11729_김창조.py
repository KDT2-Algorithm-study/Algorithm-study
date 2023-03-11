# 하노이 탑 이동 순서

n = int(input())
round = [[num for num in range(n, 0, -1)], [], []]
move = []

def recursive_hanoi(round: list, n: int, from_n: int, to_n: int, other_n: int, move: list):
    # print(round, from_n, to_n, other_n, move)
    if not n:
        return
    
    recursive_hanoi(round, n-1, from_n, other_n, to_n, move)
    round[to_n-1].append(round[from_n-1].pop())
    move.append((from_n, to_n))
    recursive_hanoi(round, n-1, other_n, to_n, from_n, move)

recursive_hanoi(round, n, 1, 3, 2, move)

print(len(move))
for t in move:
    print(*t)