import sys
input = sys.stdin.readline 

n = int(input())
li = []
for i in range(n) :
    a = input().strip()
    # print(a)
    if 'push' in a :
        a = a.replace('push ','')
        
        li.append(int(a))
        # print(li)
    elif a == 'pop' :
        if len(li) == 0 :
            print(-1)
        else :
            print(li.pop())   
            # print(li)     
    elif a == 'size' :
        print(len(li))
    elif a == 'empty' :
        if len(li) == 0 :
            print(1)
        else :
            print(0)  
    else :
        if len(li) == 0 :
            print(-1)
        else :
            li_re = li[::-1]
            print(li_re[0])                          