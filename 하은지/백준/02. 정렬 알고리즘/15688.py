# [0] 변수 선언부
import sys
T    = int(sys.stdin.readline())
list = [int(sys.stdin.readline()) for _ in range(T)]

# [1] 정렬 및 출력
list.sort(reverse = False)    # defalut value : reverse = True
for i in list:
    print(i)
