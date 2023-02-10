def bhh(a):
    b = a
    while a>0:
        b +=a%10
        a//=10  
    return(b)


a= int(input())
for i in range(a):
    if bhh(i) == a:
        print (i)
        break
else:
    print ('0')