import sys

M, N = map(int, sys.stdin.readline().split())

def isPrime(M, N):
    N += 1
    prime = [True] * N
    for i in range(2, int(N**0.5)+1):
        if prime[i]:
            for j in range(i+i, N, i):
                prime[j] = False

    for i in range(M, N):
        if i > 1 and prime[i] == True:
            print(i)

isPrime(M, N)

# def isPrime(num):
#     if num == 1:
#         return False
#     else:
#         for i in range(2, int(num**0.5)+1):
#             if num%i == 0:
#                 return False
#         return True
# 
# M, N = map(int, sys.stdin.readline().split())
# 
# for i in range(M, N+1):
#     if isPrime(i):
#         print(i)
