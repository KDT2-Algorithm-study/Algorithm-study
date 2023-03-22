def solution(quiz):
    answer = []
    for ele in quiz:
        left, right = ele.split('=')
        left = left.split()  
        right = int(right)
        
        if left[1] == '+':
            if int(left[0]) + int(left[2]) == right:
                answer.append('O')
            else:
                answer.append('X')
        elif left[1] == '-':
            if int(left[0]) - int(left[2]) == right:
                answer.append('O')
            else:
                answer.append('X')
    return answer