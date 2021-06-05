def LongestIncreasingSubsequence(numlist):
    #initalize
    T=[]
    for i in range(len(numlist)):
        T+=[1]
    #print(T)

    for i in range(1,len(numlist)):
        max_count=1
        for j in range(len(numlist)-1):
            if numlist[i] >numlist[j]:
                temp_count = T[j]+1
                if temp_count > max_count:
                    max_count = temp_count
        T[i] = max_count
    print(max(T))
    return max(T)
        
LongestIncreasingSubsequence([1,9,5,1,7])
    

def LongestIncreasingSubsequenceValue(numlist):
    #initalize
    T=[]
    for i in range(len(numlist)):
        T.append([1,[numlist[i]]])


    for i in range(1,len(numlist)):
        max_count=1
        sequencelist=[]
        for j in range(len(numlist)-1):
            if numlist[i] >numlist[j]:
                temp_count = T[j][0]+1
                if temp_count > max_count:
                    max_count = temp_count
                    sequencelist = T[j][1]
                    
        T[i][0] = max_count
        T[i][1] += sequencelist 
            
    print(max(T))
    return max(T)

LongestIncreasingSubsequenceValue([10, 22, 9, 33, 21, 50, 41, 60])
    
