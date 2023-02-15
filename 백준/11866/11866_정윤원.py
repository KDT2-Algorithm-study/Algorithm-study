'''
import sys
sys.stdin = open('test.txt', 'r')
import sys
input = sys.stdin.readline
'''
N, K= map(int,input().split())
list1 = list(range(1,N+1))

print('<', end='')

i = K - 1

while list1 :
    print(list1.pop(i), end = ', ' if list1 else '')

    i += K - 1
    while list1 and  i > (len(list1) - 1) :
        i -= len(list1)

print('>')