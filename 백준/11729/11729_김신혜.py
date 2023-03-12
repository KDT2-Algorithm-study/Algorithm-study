import sys
def hanoi(N, a, b, c):
    if N == 1:
        print(a, b)
    else:
        hanoi(N -1, a, c, b)
        print(a, b)
        hanoi(N -1, c, b, a)

N = int(sys.stdin.readline())
print((2 ** N) - 1)
hanoi(N, "1", "3", "2")

# ===========================

def 하노이탑(원판개수, 시작, 목표, 보조):
    if 원판개수 == 1:
        print(시작, "->", 목표)
    else:
        하노이탑(원판개수 - 1, 시작, 보조, 목표)
        print(시작, "->", 목표)
        하노이탑(원판개수 - 1, 목표, 보조, 시작)

원판개수 = int(sys.stdin.readline())
하노이탑(원판개수, "A", "B", "C")
