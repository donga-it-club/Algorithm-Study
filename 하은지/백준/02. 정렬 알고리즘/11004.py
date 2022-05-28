// [0] 변수 선언부 
import sys
N, K = map(int, sys.stdin.readline().split())
A    = list(map(int, sys.stdin.readline().split()))

// [1] 정렬 및 출력 
A.sort(reverse = False)
print(A[K-1])
