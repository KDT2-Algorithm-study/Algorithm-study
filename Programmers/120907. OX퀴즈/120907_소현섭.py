def solution(quiz):
    return ["X" if eval(x.split(' = ')[0]) != int(x.split(' = ')[1]) else "O" for x in quiz]