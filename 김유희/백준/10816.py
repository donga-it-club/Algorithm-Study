import sys

input = sys.stdin.readline

N = int(input())
NList = sorted(map(int, input().split()))
NDict = {}

for i in NList:
    if i not in NDict:
        NDict[i] = 1
    else:
        NDict[i] += 1

M = int(input())
MList = list(map(int, input().split()))

def binarySearch(target):
    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2
        if NList[mid] == target:
            break
        if target < NList[mid]:
            end = mid - 1
        elif target > NList[mid]:
            start = mid + 1
    if NList[mid] == target:
        print(NDict[target], end=' ')
    else:
        print(0, end=' ')

for i in range(M):
    binarySearch(MList[i])
