# 4751. 다솔이의 다이아몬드 장식

test_case = int(input())
for tc in range(1, test_case+1):
    word = input()
    line_edge = '.' + '.#..' * len(word) + '\n'
    line_middle = '.' + '#.#.' * len(word) + '\n'
    line_center = '#'
    for c in word:
        line_center += '.' + c +'.#'
    line_center += '\n'
    
    answer = line_edge + line_middle + line_center + line_middle + line_edge
    print(answer, end='')