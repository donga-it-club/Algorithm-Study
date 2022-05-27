import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    testcase = list(map(int, input().split()))
    testcase.sort()
    print(testcase[-3])
