# absolutes = [4, 7, 12]
# signs = ['true', 'false', 'true']
# result = 0

# for i in range(len(absolutes)):
#     if signs[i] == 'true':
#         result += absolutes[i] * 1
    
#     else:
#         result += absolutes[i] * -1

# print(result)

# ===============================================

def solution(absolutes, signs):
    result = 0
    for i in range(len(absolutes)):
        if signs[i] == 1:
            result += absolutes[i] * 1
    
        else:
            result += absolutes[i] * -1
    
    return result