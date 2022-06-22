import sys

input = sys.stdin.readline
INF = 10**7
numbers = [1]*INF
for i in range(2, int(INF**0.5)+1):
    if numbers[i]:
        for j in range(i+i, INF, i):
            numbers[j] = 0
prime = [i for i in range(2, INF) if numbers[i]]
K = int(input())
print(prime[K-1])    
