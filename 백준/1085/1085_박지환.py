x, y, w, h = map(int, input().split()) 
print(min(x, y, h - y, w - x)) # 직사각형 안에 한 점이 있으므로 네 변까지의 거리 중에 가장 가까운 거리가 답이다.