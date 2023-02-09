# 1085 직사각형에서 탈출

# 제한조건 1 ≤ x ≤ w-1, 1 ≤ y ≤ h-1 때문에
# (x, y)가 직사각형 밖에 있는 경우는 고려x

x, y, w, h = map(int, input().split())

li = [x, y, w-x, h-y]

print(min(li))   