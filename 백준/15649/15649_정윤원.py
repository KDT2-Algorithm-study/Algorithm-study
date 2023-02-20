from itertools import permutations
N, M = map(int, input().split())
for i in permutations(range(1, N+1), M):
    print(*i)

# 해결 못 해서 함수를 검색해서 풀었습니다.