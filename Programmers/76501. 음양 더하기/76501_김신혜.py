def solution(absolutes, signs):
    width = len(absolutes)
    answer = 0
    for w in range(width):
       if signs[w] == True:
           answer += absolutes[w]
       else:
           answer -= absolutes[w]
    return answer

print(solution([4,7,12], [True,False,True]))
print(solution([1,2,3], [False,False,True]))