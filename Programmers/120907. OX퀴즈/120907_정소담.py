def solution(quiz):
    answer = []
    for i in quiz:
        n,m = i.split('=')
        if eval(n) == int(m):
            answer.append('O')
        else:
            answer.append('X')
    return answer