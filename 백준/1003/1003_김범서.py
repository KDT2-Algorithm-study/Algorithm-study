'''
메모이제이션memoization
: 컴퓨터 프로그램이 동일한 계산을 반복해야 할 때 이전에 계산한 값을 메모리에 저장하여
동일한 계산의 반복 수행을 제거해 실행 속도를 빠르게 하는 방법
'''

def fibonacci(n):
    zero = [1, 0]    # 0의 개수를 저장하기 위한 리스트
    one = [0, 1]     # 1의 개수를 저장하기 위한 리스트
    
    if n >= 2:  # 주어진 수가 2 이상일 때
        for i in range(1, n):
            # k번째 피보나치 수열을 구할 때 1번째 수와 k-2번째 수를 더하는 것처럼
            # 리스트 zero와 one에 가장 마지막 두 원소를 더한 값을 append한다.
            zero.append(zero[i] + zero[i - 1])
            one.append(one[i] + one[i - 1])

    # 리스트 zero와 one에서 각각 인덱스 n인 원소를 출력한다.
    print(f'{zero[n]} {one[n]}')

t = int(input())

for i in range(t):
    number = int(input())
    fibonacci(number)
