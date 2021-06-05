def largestProduct(numlist):
    T =[0]
    U =[0]
    for i in range(len(numlist)):
        T+=[0]
        U+=[0]
    T[0]=1
    U[0]=1
    
    for i in range(1, len(numlist)+1):
        T[i]=max(numlist[i-1],numlist[i-1]*U[i-1],numlist[i-1]*T[i-1])
        U[i]=min(numlist[i-1],numlist[i-1]*U[i-1],numlist[i-1]*T[i-1])

    print(T)
    print(max(T[1:]))
    return max(T[1:])


largestProduct([-6,12,-7,0,14,-7,5])
