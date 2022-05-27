A = input()
T=1
for i in range(-1,-int(len(A)/2)-1,-1):
    if A[i] == A[-i-1]:
        T=1
        continue
    else:
        T=0
        break
print(T)
