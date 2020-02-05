# A = [ [1, 1, 1, 1], 
    # [2, 2, 2, 2], 
    # [3, 3, 3, 3], 
    # [4, 4, 4, 4]]
# N = 4
# for i in range(N): 
    # for j in range(i+1, N):
        # if i != j:
            # A[i][j], A[j][i] = A[j][i], A[i][j]
# print(A)
# a = [0,0,0,0]
# for i in range(4):
    # tmp = []
    # for j in range(4):
        # tmp.append(i)
    # a[i] = tmp
# print(a)

# a = [[i for j in range(4) ] for i in range(4)]
# print(a)

rotation = "clock"
n_str = 3
a = "ThisIsATestString"
if rotation == "anti":
    a = a[len(a)-n_str::] + a[:len(a)-n_str:]
elif rotation == "clock":
    a = a[n_str::] + a[:n_str:]
print(a)