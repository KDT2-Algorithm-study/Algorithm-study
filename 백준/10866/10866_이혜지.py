from collections import deque
import sys

dq = deque()

n = int(input())
for i in range(n) :
    string = sys.stdin.readline().strip()

    if '_front' in string :
        string = string.replace('pop_front','')

        if len(string) == 0:
            if len(dq) == 0 :
                print(-1)
            else :
                print(dq.popleft())  
               
        else :  
            string = string.replace('push_front ','')  
            dq.appendleft(int(string))
            
    elif '_back' in string :
        string = string.replace('pop_back','')
        if len(string) == 0: 
            if len(dq) == 0 :
                print(-1)
            else :
                print(dq.pop())  
        else :    
            string = string.replace('push_back ','')
            dq.append(int(string))

    elif 'size' == string :
        print(len(dq))        

    elif 'empty' == string :
        if len(dq) == 0 :
            print(1)    
        else :
            print(0)      

    elif 'front' == string :
        if len(dq) == 0 :
            print(-1)
        else :
            print(dq[0])    

    elif 'back' == string :
        if len(dq) == 0 :
            print(-1)
        else :
            temp = dq.pop()
            print(temp)
            dq.append(temp)

