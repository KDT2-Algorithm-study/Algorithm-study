# 음양 더하기

def solution(absolutes, signs):
    for i in range(len(absolutes)):
        if signs[i] == True:
            absolutes[i]
        else:
            absolutes[i] = -absolutes[i]
        answer = sum(absolutes)
    return answer