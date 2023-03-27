def solution(quiz):
    answer = []
    for string in quiz:
        x, sign, y, equal, z = string.split()
        if sign == "-":
            if int(z) == int(x) - int(y):
                answer.append("O")
            else:
                answer.append("X")
        elif sign == "+":
            if int(z) == int(x) + int(y):
                answer.append("O")
            else:
                answer.append("X")
        
    return answer