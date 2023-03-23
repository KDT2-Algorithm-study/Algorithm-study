def solution(quiz):
    answer, res = [], []

    for i in quiz:
        answer.append(i.split(' '))

    for j in range(len(answer)):
        if answer[j][1] == "+":
            if int(answer[j][0]) + int(answer[j][2]) == int(answer[j][4]):
                res.append("O")
            else:
                res.append("X")

        else:
            if int(answer[j][0]) - int(answer[j][2]) == int(answer[j][4]):
                res.append("O")
            else:
                res.append("X")

    return res