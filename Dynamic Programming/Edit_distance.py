def edit_distance(A,B):
    T=[]
    for a in range(len(A)+1):
        row = [0]
        for b in range(1,len(B)+1):
            if a==0:
                row.append(0)
            else:
                row.append(0)
        T.append(row)
    
    #print(T)
    
    for i in range(1,len(A)+1):
        for j in range(1,len(B)+1):
            if A[i-1] == B[j-1]:
                T[i][j] = T[i-1][j-1]+1
            else:
                #print((i,j))
                T[i][j] = max( (T[i-1][j]), (T[i][j-1]))
    

    for i in T:
        print(i)
    return T[-1][-1]

A="APPLE"
B = "ELPPA"
#A="CTGCG"
#B = "GTCG"
print(edit_distance(A,B))
