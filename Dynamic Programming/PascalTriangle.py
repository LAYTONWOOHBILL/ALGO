def PascalTriangle(i,j):
    if j == 1:
        return 1
    if i == j:
        return 1
    return Pascal_Triangle(i-1,j-1) + Pascal_Triangle(i-1,j)        
            


print(Pascal_Triangle(6,4))
#print(Pascal_Triangle(2,1),Pascal_Triangle(2,2))
#print(Pascal_Triangle(3,1),Pascal_Triangle(3,2),Pascal_Triangle(3,3))
#print(Pascal_Triangle(4,1),Pascal_Triangle(4,2),Pascal_Triangle(4,3),Pascal_Triangle(4,4))


def dp_PascalTriangle(i,j):
    T=[]
    for a in range(i):
        row = []
        for b in range(j):
            if a == b or b == 0:
                row.append(1)
            else:
                row.append(0)
        T.append(row)
    
    for row in range(1,i):
        for col in range(1,j):
          T[row][col] = T[row-1][col-1]+ T[row-1][col]

    return T[i-1][j-1]

print(dp_Pascal_Triangle(6,4))
