W = input().upper()
D = {}
for i in range(len(W)):
    if W[i] not in D:
        D[W[i]] = 1
    else:
        D[W[i]] += 1
M = max(D,key=D.get)
MN= D[M]
del D[M]
for i in D:
    if  MN== D[i]:
        print("?")
        exit()
print(M)
