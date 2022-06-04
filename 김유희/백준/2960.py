import sys

N, K = map(int, sys.stdin.readline().split())
numbers = [i for i in range(2, N+1)]
deleteNums = []

while numbers:
    deleteNum = numbers.pop(0)
    deleteNums.append(deleteNum)

    temp = deleteNum
    while temp <= N:
        if temp in numbers:
            numbers.remove(temp)
            deleteNums.append(temp)
        temp += deleteNum

print(deleteNums[K-1])
