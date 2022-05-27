import sys

input()

A = list(map(int, input().split()))
B = sorted(A)
P = []

for i in A:
    P.append(B.index(i))
    B[B.index(i)] = -1

for i in P:
    sys.stdout.write(str(i)+' ')
