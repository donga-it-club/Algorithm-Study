import sys

input = sys.stdin.readline

N, M = map(int, input().split())
NList = [input().rstrip() for _ in range(N)]
MList = [input().rstrip() for _ in range(M)]

listenSee = sorted(list(set(NList) & set(MList))) #교집합

print(len(listenSee))
print("\n".join(listenSee))
