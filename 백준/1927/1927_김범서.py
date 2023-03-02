import heapq, sys

n = int(sys.stdin.readline())
heap = list()

for i in range(n):
    # 정수를 입력한다
    x = int(sys.stdin.readline())
    # 0인 경우
    # 배열이 비어있으면 0
    # 비어있지 않으면 pop 메서드를 사용해 가장 작은 원소를 제거하며 출력한다
    # sys.stdout.write는 개행문자 없이 출력하기 때문에
    # 끝에 개행문자를 추가하기 위해 f-string을 사용했다
    if not x:
        try:
            sys.stdout.write(f'{heapq.heappop(heap)}\n')
        except:
            sys.stdout.write(f'0\n')
    # 0이 아닌 경우
    # 배열에 정수를 넣는다
    else:
        heapq.heappush(heap, x)

'''
백준 온라인 저지에서 Python3 옵션 기준
print를 사용했을 때 180ms
sys.stdout.write를 사용했을 때 136ms
메모리 사용량은 37180kB로 같았다
'''
