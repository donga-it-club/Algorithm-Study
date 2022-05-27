# [0] 변수 선언부 
import sys
user = list(map(int, sys.stdin.readline().split()))
user = sorted(user)

# [1] 출력
print(*user)
