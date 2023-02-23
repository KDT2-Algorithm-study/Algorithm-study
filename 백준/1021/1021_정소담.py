# 1안
from collections import deque
n,m = map(int,input().split())
lst = deque(range(1,n+1))
lst2 = deque(range(1,n+1))
num = list(map(int,input().split()))
answer = 0

for i in num:
    cnt = 0
    cnt2 = 0
    while 1:
        if lst[0] == i:
            lst.popleft()
            break
        lst.rotate(1)
        cnt += 1
    while 1:
        if lst2[0] == i:
            lst2.popleft()
            break
        lst2.rotate(-1)
        cnt2 += 1
    answer += min(cnt,cnt2)
print(answer)
# 제목 그대로 큐를 회전시켜서 푼 방법
# 왼쪽으로 돌렸을 때 오른쪽으로 돌렸을 때 중 회전수가 작은 것을 더 해 출력

# 2안 
n,m = map(int,input().split())
lst = list(range(1,n+1))
num = list(map(int,input().split()))
cnt = 0

for i in num:
    x = lst.index(i) # 찾는 숫자의 인덱스
    cnt += min(x,len(lst)-x) # 앞에서 부터의 위치, 뒤에서 부터의 위치 중 작은 것을 더함
    lst = lst[x+1:] + lst[:x] # 찾은 숫자 뒷자리부터 끝까지 + 찾은 숫자 앞자리까지
    # 찾은 숫자는 리스트에서 제외 시키고 로테이션 한것 처럼 리스트를 다시 만들어줌
print(cnt)
