T = int(input())

for _ in range(T):
    words = input()
    n = len(words)

    print('.'+'.#..' * n)
    print('.'+'#.#.' * n)

    for i in words:
        print(f'#.{i}.', end='')

    print('#')
    print('.'+'#.#.' * n)
    print('.'+'.#..' * n)
