import sys
input = sys.stdin.readline

N = int(input())
NList = sorted(map(int,stdin.readline().split()))
M = int(input())
MList = sorted(map(int,stdin.readline().split()))

def binarySearch(target):
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2
        if n_list[mid] == target:
            return True

        if target < n_list[mid]:
            right = mid-1
        elif target > n_list[mid]:
            left = mid + 1
            
for i in range(M):
    if binary(MList[i]):
        print(1)
    else:
        print(0)
    
