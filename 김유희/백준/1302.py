import sys
input = sys.stdin.readline

N = int(input())
bestseller = {}
for i in range(N):
    name = input()
    if name in bestseller:
        bestseller[name] += 1
    else:
        bestseller[name] = 1

bestseller = sorted(bestseller.items(), key = lambda x : (-int(x[1]), x[0]))

print(bestseller[0][0])
