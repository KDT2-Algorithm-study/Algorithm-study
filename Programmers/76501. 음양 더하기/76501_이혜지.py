def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)) :
        if signs[i] == True :
            answer += absolutes[i]
        else :
            answer -= absolutes[i]      
    return answer


absolutes_li = list(map(int, input().split()))
signs_li = list(input().split())

print(solution(absolutes_li, signs_li))