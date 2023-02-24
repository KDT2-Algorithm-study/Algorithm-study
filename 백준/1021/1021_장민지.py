# # 1. 처음 푼 방법( pop(o)는 알고리즘에서 좋지 못한 방법이라 하여 덱을 사용하는 코드를 참고해서 다시 풀어봤다.)
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
# # 두 코드의 시간 복잡도가 크지 않아서 찾아보다보니 알게 된 사실이...
# # deque는 블럭 단위로 연결된 링크드 리스트 형태라 특정 인덱스로의 임의 접근은 O(n)이 걸린다. 하지만 리스트.index의 시간 복잡도는 O(1)이다.
# # 하지만 이 문제는 M의 값이 크지 않기에, 덱을 사용하더라도 두 코드의 시간 복잡도의 차이가 크게 나지 않는 것 같다.


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
