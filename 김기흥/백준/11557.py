T = int(input())
best = []
for i in range(T):
    N = int(input())
    S = []
    L = []
    for j in range(N):
        s, l = input().split()
        S.append(s)
        L.append(l)
    best.append(S[L.index(str(max(list(map(int,L)))))])
print(*best,sep = '\n')
