from collections import deque

# priorities [1, 1, 9, 1, 1, 1]
# location 0
def solution(priorities, location):

    '''@enumerate(iterable) 내장함수: (인덱스값, 요소)를 튜플 형식으로 돌려줌'''
    # [(0,1), (1,1), (2, 9), (3,1), (4,1), (5,1)]
    printer = [ (i,p) for i,p in enumerate(priorities)]
    answer = 0


    while printer: # printer에 요소가 남지 않을 때까지 반복한다.
        first = printer.pop(0) # 맨 앞에 있는 요소부터 확인한다.

        ''' any(iterable) 내장함수: 입력받은 요소에서 하나라도 참이면 True'''
        # printer에서 요소를 하나씩 꺼내오는데,
        # 맨 앞에 있는 요소보다 높은 수가 하나라도 있다면(True)
        # printer의 뒤에 넣는다.
        if any(first[1] < other[1] for other in printer):
            printer.append(first)

        # 맨 앞에 있는 요소가 제일 크다면(방금 pop한 요소가 제일 크다면)
        # 출력횟수를 카운트하여 +1 한다.
        else:
            answer += 1

            # pop한 뒤 [0]번 인덱스가 내가 찾는 값인지 확인하고 break
            if first[0] == location: 
                break
            
    return answer


print(solution([1, 1, 9, 1, 1, 1], 0)) # 5
print(solution([2, 1, 3, 2], 2)) # 1
print(solution([1, 2, 3, 4, 5, 6], 0))  # 6

# 런타임 에러