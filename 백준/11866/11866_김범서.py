from collections import deque

n, k = map(int, input().split())
people = deque([x for x in range(1, n + 1)])
result = list()

# deque의 rotate 메서드를 이용해 배열을 회전시킨다.
while people:
    people.rotate(-k)
    result.append(people.pop())

print('<', end = '')
print(*result, sep = ', ', end = '')
print('>')
