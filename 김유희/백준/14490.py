import sys

input = sys.stdin.readline

A,B = map(int, input().split(":"))
a,b = A,B

while b != 0:
    a = a % b
    a,b = b,a

print(f"{A//a}:{B//a}")
