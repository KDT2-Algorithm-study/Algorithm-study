x, y, w, j = map(int, input().split())

print(min(x, y, w-x, j-y))