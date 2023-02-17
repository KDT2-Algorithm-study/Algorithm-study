for _ in range(int(input())):
    h, w, n = map(int, input().split())
    front_num = n % h
    back_num = (n // h) + 1
    if front_num == 0:
        front_num = h
        back_num -= 1
    print((front_num * 100) + back_num)