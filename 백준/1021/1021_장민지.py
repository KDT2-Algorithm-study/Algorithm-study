# # 1. 처음 푼 방법
# # 이번 문젠 범위가 넓지 않아서 차이가 크게 없지만 pop(0)를 쓰게 되니 알고리즘에 적합하지 않음....
# N, M = map(int, input().split())
# num_list = list(i for i in range(1, N+1))
# numbers = list(map(int, input().split()))
# cnt = 0
# for i in numbers:
#     while True:
#         if num_list[0] == i:
#             num_list.pop(0)
#             break
#         else:
#             n = num_list.index(i)
#             if len(num_list[:n]) <= len(num_list[n+1:]):
#                 num_list.append(num_list.pop(0))
#                 cnt += 1
#             else:
#                 num_list.insert(0, num_list.pop())
#                 cnt += 1
# print(cnt)


# 2. 태양님 코드를 참고하여(if절의 범위 설정) 덱 사용!
from collections import deque

N, M = map(int, input().split())
num_deque = deque(i for i in range(1, N+1))
numbers = list(map(int, input().split()))
cnt = 0

for i in numbers:
    while True:
        if num_deque[0] == i:
            num_deque.popleft()
            break
        else:
            if num_deque.index(i) < len(num_deque) / 2:
                num_deque.append(num_deque.popleft())
                cnt += 1
            else:
                num_deque.appendleft(num_deque.pop())
                cnt += 1
print(cnt)