def solution(quiz):
    answer = list()

    for equation in quiz:
        elements = equation.split()
        # eval()을 사용해 등호 전까지의 식을 계산한다.
        result = eval(''.join(elements[:-2]))

        # 등호 이후의 값과 위에서 계산한 것을 비교한다.
        if result == int(elements[-1]):
            answer.append("O")
        else:
            answer.append("X")

    return answer
