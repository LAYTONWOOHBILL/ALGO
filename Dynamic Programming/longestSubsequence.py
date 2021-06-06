def longestSubsequence(numlist):
    #inti
    T=[]
    for i in range(len(numlist)):
        T.append([1,[numlist[i]]])
    print(T)

    for i in range(1,len(numlist)):
        max_value = 1
        pointer = -1
        for j in range(i):
            if numlist[j] < numlist[i] and T[j][0]+1 > max_value:
                max_value = T[j][0]+1
                pointer = j
        T[i][0] = max_value
        if pointer > 0:
            T[i][1] += T[pointer][1]

    #for i in T:
    #    print(i)
    print(max(T))
    return max(T)
                
longestSubsequence([5, 2, 8, 6, 3, 6, 9, 7])
