T = int(input())

for i in range(T):
    word = input()
    a, b, c = '.', '.', '#'

    for i in word:
        a += '.#..'
        b += '#.#.'
        c += f'.{i}.#'

    print(a, b, c, b, a, sep='\n')
