cnt = 0
change = 0
def heapify(A, k, n) :
    global cnt
    global change
    left = 2*k                          # k 왼쪽 자식 노드
    right =2*k + 1                      # k 오른쪽 자식 노드
    smaller = 0                         # 왼쪽과 오른쪽 중에 작은놈 체크
    if right <= n :                     # 자식노드가 둘다 있을 때
        if A[left] < A[right] :
            smaller = left
        else: 
            smaller = right                
    elif left <= n :                    # 왼쪽 자식노드만 있을 때
        smaller = left
    else :
        return
    
    if A[smaller] < A[k] :
        if k!=n:
            cnt+=1
            # print('heapify')
            # print(k,n)
        if cnt==change:
            print(min(A[k],A[smaller]),max(A[k],A[smaller]))
        A[k],A[smaller] = A[smaller],A[k]
        heapify(A,smaller,n)


def build_min_heap(A, n): 
        for i in range(int(n/2),0,-1):
            heapify(A, i, n)

def heap_sort(A):
        global cnt
        global change
        build_min_heap(A, len(A)-1)
        for i in range(len(A)-1, 1,-1): 
            if i!=1:
                cnt +=1
                # print('1과i 교환')
                # print(1,i)
            if cnt == change:
                print(min(A[1],A[i]),max(A[1],A[i]))
            A[1],A[i] = A[i],A[1]
            heapify(A, 1, i - 1)
               

# n = 5
# k = 10
# A = [0, 2, 5, 1, 4, 3]
# heap_sort(A)


n, change = map(int,input().split())
A = [0]+list(map(int,input().split()))
heap_sort(A)
if change>cnt:
    print(-1)
