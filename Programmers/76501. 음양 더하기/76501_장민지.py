def solution(absolutes, signs):
    for i in range(len(absolutes)):
        if signs[i] == False:
            absolutes[i] = -absolutes[i]
    answer = sum(absolutes)
    return answer