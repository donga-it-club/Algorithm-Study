# ---------------------------------------------------
# [1368ms]

# [0] 변수 선언부
import sys
T = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(T)]

# [1] 정렬 및 출력
nums.sort(reverse = True)
for num in nums:
    print(num)
#---------------------------------------------------


#---------------------------------------------------
# [1380ms]

# [0] 변수 선언부
import sys
input = sys.stdin.readline
T = int(input())
nums = [int(input()) for _ in range(T)]

# [1] 정렬 및 출력
nums.sort(reverse = True)
for num in nums:
    print(num)
#---------------------------------------------------


#---------------------------------------------------
# [1448ms]

# [0] 변수 선언부
import sys
T    = int(sys.stdin.readline())
nums = []

for _ in range(T):
    nums.append(int(sys.stdin.readline()))

# [1] 정렬 및 출력
nums.sort(reverse = True)
for num in nums:
    print(num)
#---------------------------------------------------


#---------------------------------------------------
# [1464ms]

# [0] 변수 선언부
import sys
T    = int(sys.stdin.readline())
nums = []

for _ in range(T):
    nums.append(int(sys.stdin.readline()))

# [1] 정렬 및 출력
for num in reversed(sorted(nums)):
    print(num)
#---------------------------------------------------


#---------------------------------------------------
# [1508ms]

# [0] 변수 선언부
import sys
T    = int(sys.stdin.readline())
list = []

# [1] 정렬 및 출력
for _ in range(T):
    list.append(int(sys.stdin.readline()))

for i in reversed(sorted(list)):
    print(i)
#---------------------------------------------------
