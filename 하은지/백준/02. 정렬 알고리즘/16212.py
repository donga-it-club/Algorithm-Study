# [0] 변수 선언부
N = int(input())
a = list(map(int, input().split()))

# [1] 정렬 및 출력 
a.sort(reverse = False)
print(*a, sep = " ")
