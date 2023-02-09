# import sys
# sys.stdin = open('test.txt', 'r')

x, y, w, h = map(int, input().split())

dist_x = w-x if x > w/2 else x
dist_y = h-y if y > h/2 else y
print(min(dist_x,dist_y))