def binomialCoefficient(n,k):
    l = [[0]*(k+1) for i in range(n+1)]
    for i in range(n+1):
        for j in range(min(i,k)+1):
            if j==0 or j==i:
                l[i][j] = 1
            else:
                l[i][j] = l[i-1][j-1] + l[i-1][j]
    return l[n][k]

print(binomialCoefficient(5,2))