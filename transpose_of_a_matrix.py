A = [ [1, 1, 1, 1], 
    [2, 2, 2, 2], 
    [3, 3, 3, 3], 
    [4, 4, 4, 4]]
N = 4
for i in range(N): 
    for j in range(i+1, N):
        if i != j:
            A[i][j], A[j][i] = A[j][i], A[i][j]
print(A)
