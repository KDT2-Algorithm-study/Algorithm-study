i = int(input())

pro = 1

if i == 0 :
    print(1)

else :
    while True :
        if i == 1 :
            print(pro)
            break
        else :
            pro *= i
            i -= 1    