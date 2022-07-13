import sys

input = sys.stdin.readline

N = int(input())
NList = sorted(map(int, input().split()))
M = int(input())
MList = list(map(int, input().split()))


def binarySearch(target):
    left = 0
    right = N - 1

    while left <= right:
        mid = (left + right) // 2
        if NList[mid] == target:
            return True

        if target < NList[mid]:
            right = mid - 1
        elif target > NList[mid]:
            left = mid + 1


for i in range(M):
    if binarySearch(MList[i]):
        print(1)
    else:
        print(0)
