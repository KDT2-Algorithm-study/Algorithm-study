import sys

def heap_sort(a, n):
    global c
    build_min_heap(a, n)
    for i in range(n-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        c += 1
        if c == K:
            answer.extend([a[0], a[i]])
        heapify(a, 0, i)

def build_min_heap(a, n):
    for i in range((n//2), -1, -1):
        heapify(a, i, n)

def heapify(a, k, n):
    global c
    l = 2 * k + 1
    r = 2 * k + 2
    if l < n and a[l] < a[k]:
        smaller = l
    else:
        smaller = k
    if r < n and a[r] < a[smaller]:
        smaller = r
    if smaller != k:
        a[k], a[smaller] = a[smaller], a[k]
        c += 1
        if c == K:
            answer.extend([a[k], a[smaller]])
        heapify(a, smaller, n)

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
c = 0
answer = []
heap_sort(A, N)
print('-1') if not answer else print(*sorted(answer))