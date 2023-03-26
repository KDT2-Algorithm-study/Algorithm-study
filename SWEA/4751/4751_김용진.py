# 다솔이의 다이아몬드 장식
# 태양님 코드를 참고해서 풀어 보았습니다

import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):
    word = input()
    n = len(word) 

    for i in range(n):
        print("..#.", end="")
        if i == n-1:
            print(".")
    for i in range(n):
        print('.#.#',end='')
        if i == n-1:
            print('.')
    
    for i in range(n):
        print('#.'f'{word[i]}.',end='')
        if i == n-1:
            print('#')
    
    for i in range(n):
        print('.#.#',end='')
        if i == n-1:
            print('.')

    for i in range(n):
        print("..#.", end="")
        if i == n-1:
            print(".")