import sys

input = sys.stdin.readline

N = 123456 * 2 + 1

numCheck = [True] * N
for i in range(2, int(N**0.5)+1):
    if numCheck[i]:
        for j in range(i+i, N, i):
            numCheck[j] = False

def prime_cnt(val):
    cnt = 0
    for i in range(val + 1, val * 2 + 1):
        if numCheck[i]:
            cnt += 1
    print(cnt)

while True:
    val = int(input())
    if val == 0:
        break
    prime_cnt(val)
