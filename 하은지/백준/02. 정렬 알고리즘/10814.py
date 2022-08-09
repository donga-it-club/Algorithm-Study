import sys

N = int(sys.stdin.readline())
List = []

for i in range(N):
    old, name = sys.stdin.readline().split()
    List.append([int(old), name])

List.sort(key = lambda x : x[0])

for i in range(N):
    print(List[i][0], List[i][1])
