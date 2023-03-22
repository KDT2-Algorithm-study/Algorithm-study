def solution(quiz):
    answer = []
    for formula in quiz:
        x, cal, y, e, result = formula.split()
        x = int(x)
        y = int(y)
        result = int(result)
        if cal == '+':
            if (x + y) == result:
                answer.append('O')
            else:
                answer.append('X')
        else:   # cal == '-'
            if (x - y) == result:
                answer.append('O')
            else:
                answer.append('X')
    
    return answer