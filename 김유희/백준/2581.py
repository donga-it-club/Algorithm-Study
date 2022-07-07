import sys
input = sys.stdin.readline
M = int(input())
N = int(input())

min = 0
sum = 0

N += 1
prime = [True] * N
for i in range(2, int(N**0.5)+1):
    if prime[i]:
        for j in range(i+i, N, i):
            prime[j] = False

for i in range(M, N):
    if i > 1 and prime[i] == True:
        sum += i
        if min == 0:
            min = i

if sum == 0:
    print(-1)

else :
    print(sum); print(min)
