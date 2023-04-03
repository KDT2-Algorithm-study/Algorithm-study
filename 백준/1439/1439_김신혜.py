# 가장 빨리 이해가 되었던 지환님 풀이를 참고했습니다.
import sys
words = sys.stdin.readline()
cnt0 = 0
cnt1 = 0
change = '2'

for i in words:
    if i != change:
        if i == '0':
            cnt0 += 1
            change = '0'
        elif i == '1':
            cnt1 += 1
            change = '1'
print(min(cnt0, cnt1))