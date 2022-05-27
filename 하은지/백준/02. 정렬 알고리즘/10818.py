# [0] 변수 선언부 
import sys
T    = int(sys.stdin.readline())
user = list(map(int, sys.stdin.readline().split()))

# [1] 출력
print(min(user), max(user))
