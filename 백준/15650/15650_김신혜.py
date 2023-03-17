import sys
N, M  = map(int,sys.stdin.readline().split())
ans = []

def backtracking(n, lst):   # 1과 빈 리스트 입력받음
    if n > N :
        if len(lst) == M:   # 비어있던 리스트가 가득 채워지면 
            ans.append(lst) # ans라는 리스트에 추가됨
        return
    backtracking(n + 1, lst + [n])
    backtracking(n + 1, lst)

backtracking(1, [])
for lst in ans:
    print(*lst)
