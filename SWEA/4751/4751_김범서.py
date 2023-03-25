t = int(input())

for i in range(t):
    word = input()
    result = ['' for i in range(5)]

    result[0] = '..' + '#...' * (len(word) - 1) + '#..'
    result[1] = '.#' + '.#.#' * (len(word) - 1) + '.#.'
    result[3] = '.#' + '.#.#' * (len(word) - 1) + '.#.'
    result[4] = '..' + '#...' * (len(word) - 1) + '#..'

    result[2] += '#'
    for j in range(len(word)):
        result[2] += '.' + word[j] + '.#'

    for j in range(5):
        print(*result[j], sep='')
