# [0] 변수 선언부
import sys
T    = int(sys.stdin.readline())
list = []

# [1] 정렬 후 출력
for i in range(T):
    user = int(sys.stdin.readline())
    list.append(user)

list = sorted(list)
print(*list, sep = "\n")
