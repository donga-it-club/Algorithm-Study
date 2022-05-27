# [0] 변수 선언부
import sys
string = sys.stdin.readline().strip()
list   = [i for i in string]

# [1] 정렬 및 출력
list.sort(reverse = True)
for j in list:
    print(j, end="")
