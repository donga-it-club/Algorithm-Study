import sys

input = sys.stdin.readline

W = sorted([int(input()) for _ in range(10)], reverse = True)[:3]
K = sorted([int(input()) for _ in range(10)], reverse = True)[:3]
print(sum(W) , sum(K))
