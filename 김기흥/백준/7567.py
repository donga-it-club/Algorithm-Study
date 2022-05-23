A = input()
height = 10

for i in range(1,len(A)):
    if A[i-1] == A[i]:height +=5
    else: height+=10

print(height)
