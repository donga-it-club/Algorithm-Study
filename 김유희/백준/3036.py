import sys

input = sys.stdin.readline

N = int(input())

rings = list(map(int, input().split()))

for i in range(N-1):
    A = rings[0]
    B = rings[i+1]
    a,b = A,B
    while b != 0:
        a = a % b
        a,b = b,a
    print(f"{A//a}/{B//a}")
