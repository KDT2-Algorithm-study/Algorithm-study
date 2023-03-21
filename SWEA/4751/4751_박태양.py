for i in range(int(input())):
    s = input()
    n = len(s)

    for _ in range(n):
        print('..#.',end='')
    print('.')

    for _ in range(2*n):
        print('.#',end='')
    print('.')

    for i in s:
        print(f'#.{i}.',end='')
    print('#')

    for _ in range(2*n):
        print('.#',end='')
    print('.')

    for _ in range(n):
        print('..#.',end='')
    print('.')