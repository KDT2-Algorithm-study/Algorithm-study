def solution(quiz):
    answer = []
    for i in quiz:
        x,operation,y,equal,z = i.split()
        if operation == '+':
            if int(x)+int(y) == int(z):
                answer.append('O')
            else:
                answer.append('X')
        else:
            if int(x)-int(y) == int(z):
                answer.append('O')
            else:
                answer.append('X')   

    
    return answer

q = ["3 - 4 = -3", "5 + 6 = 11"]
print(solution(q))