# 1085. 직사각형에서 탈출
import sys


# input
x_num, y_num, w_num, h_num = map(int, sys.stdin.readline().split())


# solution
distance_width_num = w_num - x_num if w_num <= 2*x_num else x_num
distance_height_num = h_num - y_num if h_num <= 2*y_num else y_num


print(distance_width_num if distance_width_num < distance_height_num else distance_height_num)