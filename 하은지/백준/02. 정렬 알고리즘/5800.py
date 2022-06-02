# [0] 변수선언부
import sys
x = int(sys.stdin.readline())

# [1] 입력 및 정렬 
for i in range(x):
    a = list(map(int, sys.stdin.readline().split()))
    del a[0]
    a.sort()
    diff = []

    for j in range(len(a) - 1):
        diff.append(a[j+1] - a[j])
        
# [2] 출력
    print("Class", i+1)
    print("Max %d, Min %d, Largest gap %d" % (max(a), min(a), max(diff)))
