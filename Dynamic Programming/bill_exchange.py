'''
In a previous life, you worked as a cashier in the lost Antarctican colony,
spending the better part of your day giving change to your customers.
Because paper is a very rare and valuable resource in Antarctica,
cashiers were required by law to use the fewest bills possible whenever they gave change.
The currency of the colony was available in the following denominations: 1, 4, and 6
'''

def bill(total):
    return change(total,[1,4,6])

def change(total,changetypes):

    T = [0]

    for i in range(1,total+1):
        T.append(i)    
        
    for i in range(1,len(T)):
        for j in changetypes:
            if T[i-j] >= 0 and T[i-j]+1 < T[i]:
                T[i]= T[i-j]+1
    return T[-1]

print(bill(20))  
