'''
Call a sequence X[1..n] of numbers bitonic if there is an index i with 1 < i < n ,
such that the prefix X[1..i] is increasing and the suffix X[i..n] is decreasing.
Describe an efficient algorithm to compute the length of the longest bitonic subsequence of an arbitrary array A of integers.
'''
def bitoniclongestSubsequence(numlist):
    inc = []
    dec = []

    for i in range(len(numlist)):
        inc+=[1]
        dec += [1]


    for  i in range(1,len(numlist)):
        for j in range(i):
            if numlist[i]>numlist[j] and inc[j]+1>inc[i]:
                inc[i] = inc[j]+1

    for  i in range(len(numlist)-1,0,-1):
        for j in range(len(numlist)-1,i,-1):
            if numlist[i]>numlist[j] and dec[j]+1>dec[i]:
                dec[i] = dec[j]+1

    #print(inc)
    #print(dec)
    maxrange=inc[0]+dec[0]-1
    for i in range(1,len(inc)):
        if inc[i]+dec[i]-1 > maxrange:
            maxrange = inc[i]+dec[i]-1
    #print(maxrange)

bitoniclongestSubsequence([5, 2, 8, 6, 3, 6, 9, 7])
