import sys
input = sys.stdin.readline
N = int(input())
myCard = sorted(map(int, input().split()))
M = int(input())
numCard = list(map(int, input().split()))

#이분탐색
for i in numCard:
    start, end = 0, N
    while start <= end:
        mid = (start + end) // 2
        if 0 <= mid < N:
            if myCard[mid] < i: 
                start = mid + 1
            else: 
                end = mid - 1
        else: 
            break
    if 0 <= end + 1 < N:
        if myCard[end + 1] == i: 
            print(1, end=" ")
        else: 
            print(0, end=" ")
    else: 
        print(0, end=" ")
