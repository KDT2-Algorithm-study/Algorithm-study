# ox 퀴즈

def solution(quiz):
    result = []
    for i in quiz:
        left, right = i.split('=')
        left = left.split()
        if left[1] == '+':
            if int(left[0]) + int(left[2]) == int(right):
                result.append('O')
            else:
                result.append('X')
        elif left[1] == '-' :
            if int(left[0]) - int(left[2]) == int(right):
                result.append('O')
            else:
                result.append('X')
    return result