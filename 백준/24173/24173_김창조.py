# 24173. 힙 정렬 1

n, key = map(int, input().split())
lst = list(map(int, input().split()))

cnt = 0
result = -1

def heapify(A, k, n):
    global cnt, result, key
    
    left = 2*k
    right = 2*k + 1
    
    if right <= n:
        if A[left - 1] < A[right - 1]:
            smaller = left
        else:
            smaller = right
    elif left <= n:
        smaller = left
    else:
        return
    
    if A[smaller - 1] < A[k - 1]:
        cnt += 1
        if cnt == key:
            result = A[smaller - 1], A[k - 1]
            
        A[k - 1], A[smaller - 1] = A[smaller - 1], A[k - 1]
        heapify(A, smaller, n)

def build_min_heap(A, n):
    for i in range(n // 2, 0, -1):
        heapify(A, i, n)

def heap_sort(A, n):
    global cnt, result, key
    
    build_min_heap(A, n)
    for i in range(n, 1, -1):
        cnt += 1
        if cnt == key:
            result = A[0], A[i - 1]
            
        A[0], A[i - 1] = A[i - 1], A[0]
        heapify(A, 1, i - 1)
    
heap_sort(lst, n)

if result == -1:
    print(-1)
else:
    print(*result)