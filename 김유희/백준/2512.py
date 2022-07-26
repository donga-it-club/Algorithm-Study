import sys

input = sys.stdin.readline

N = int(input())
requests = list(map(int, input().split()))
budgets = int(input())

start, end = 0, max(requests)

while start <= end:
  mid = (start + end) // 2
  total = 0
  
  for i in requests:
    if i >= mid:
      total += mid
    else:
      total += i
  if total <= budgets:
    start = mid + 1
  else:
    end = mid - 1

print(end) 
