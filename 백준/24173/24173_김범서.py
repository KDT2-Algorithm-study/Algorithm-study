# 의사코드를 변환한다
def heap_sort(lst):
    global cnt
    build_min_heap(lst, n)
    for i in range(n, 1, -1):
        cnt += 1
        if cnt == target:
            print(min(lst[1], lst[i]), max(lst[1], lst[i]))
        lst[1], lst[i] = lst[i], lst[1]
        heapify(lst, 1, i - 1)

def build_min_heap(lst, n):
    for i in range(n // 2, 0, -1):
        heapify(lst, i, n)

def heapify(lst, k, n):
    global cnt
    left = 2 * k
    right = 2 * k + 1
    if right <= n:
        if lst[left] < lst[right]:
            smaller = left
        else:
            smaller = right
    elif left <= n:
        smaller = left
    else:
        return
    
    if lst[smaller] < lst[k]:
        cnt += 1
        if cnt == target:
            print(min(lst[k], lst[smaller]), max(lst[k], lst[smaller]))
        lst[k], lst[smaller] = lst[smaller], lst[k]
        heapify(lst, smaller, n)

n, target = map(int, input().split())
# 주어진 의사코드에서 행렬 인덱스가 1부터 시작했기 때문에
# 입력받은 숫자 행렬 앞에 0을 추가했다
a = [0] + list(map(int, input().split()))
# 숫자가 바뀌는 횟수를 저장하기 위한 변수
cnt = 0
# 힙 정렬 시행
heap_sort(a)
# 힙 정렬이 끝났을 때 총 교환횟수가 요구된 숫자보다 작을 경우
# -1을 출력한다
if cnt < target:
    print(-1)
