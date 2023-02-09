x, y, w, h = map(int, input().split())
xw = w - x
yh = h - y
print(min(x, y, xw, yh))