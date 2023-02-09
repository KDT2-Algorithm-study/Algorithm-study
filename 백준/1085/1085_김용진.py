# 직사각형에서 탈출
import sys
sys.stdin = open('input.txt','r')

x, y, w, h = map(int,input().split()) # 문제에 주어진 x,y,w,h에 각각의 값 정수로 입력
value = [] # 값을 담을 리스트
value.append(x) # (x,y)-(0,0) 즉 (x,y) 그대로 append 이기에 각각 append
value.append(y)
value.append(w-x) # (w,h)-(x,y)
value.append(h-y)
print(min(value)) # 리스트 value중 가장 작은수 출력 