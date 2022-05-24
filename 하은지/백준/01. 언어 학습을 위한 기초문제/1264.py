# [0] 변수 선언부 
import sys
count   = 0

# [1] 값 입력 & 출력
while (1):
    user = sys.stdin.readline().replace(' ', '').replace('\n', '')

    if (user == "#"):
        break
    
    for i in [ 'a', 'e', 'i', 'o', 'u']:
        count += user.count(i) + user.count(i.upper())

    print(count)
    count = 0
