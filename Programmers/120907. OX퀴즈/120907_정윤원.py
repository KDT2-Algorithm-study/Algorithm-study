def solution(quiz):
    for i in range(len(quiz)):
        before, after = quiz[i].split('=')
        bf_split = before.split()

        if bf_split[1] == '+':
            result = int(bf_split[0]) + int(bf_split[2])
        else:  # bf_split == '-'
            result = int(bf_split[0]) - int(bf_split[2])

        quiz[i] = 'O' if result == int(after) else 'X'

    return quiz