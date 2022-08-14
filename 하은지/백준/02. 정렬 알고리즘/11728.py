# [방법 1] 
# ---------------------------------------------------------------------
import sys
import itertools

N, M     = map(int, sys.stdin.readline().split())
A        = []
B        = []
Result_1 = []
Result_2 = []
String = ""

A.append(list(map(int, sys.stdin.readline().split())))
B.append(list(map(int, sys.stdin.readline().split())))


Result_1 = A + B

for i in Result_1:
    Result_2.extend(i)

Result_2.sort()

for i in Result_2:
    print(i, end=" ")
# ---------------------------------------------------------------------



# [방법 2] 
# ---------------------------------------------------------------------
import sys
import itertools

N, M  = map(int, sys.stdin.readline().split())
A     = list(map(int, sys.stdin.readline().split()))
B     = list(map(int, sys.stdin.readline().split()))

Result = A + B
Result.sort()

for i in Result:
    print(i, end=" ")   
# ---------------------------------------------------------------------
