
def largest_sum(A):
    
    final_max= 0
    temp_max = 0

    for i in A:
        temp_max = temp_max + i
        if temp_max < 0:
            temp_max = 0

        if temp_max > final_max:
            final_max = temp_max

    return final_max


A=[-6, 12, -7, 0, 14, -7, -5, 30]
print(largest_sum(A))


def largest_sum_memo(A):
    memo = []
    temp_max = 0

    for i in range(len(A)):
        temp_max = temp_max + A[i]
        if temp_max < 0:
            memo.append(0)
            temp_max = 0
        else:
            memo.append(temp_max)
    return max(memo)

A=[-6, 12, -7, 0, 14, -7, -5, 30]
print(largest_sum_memo(A))


'''
def largest_sum(A):
    
    final_max= 0
    temp_max = 0

    for i in A:
        if temp_max + i > 0:
            temp_max = temp_max + i
            if temp_max > final_max:
                final_max = temp_max
        else:
            temp_max = 0

    return final_max
'''
