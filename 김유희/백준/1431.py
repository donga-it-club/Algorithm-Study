import sys
input = sys.stdin.readline

def sum_intserial(serialnum):
    sum = 0
    for i in serialnum:
        if i.isdigit():
            sum += int(i)
    return sum

N = int(input().rstrip())
seriallist = []

for _ in range(N):
    seriallist.append(input().rstrip())

seriallist.sort(key = lambda x : (len(x), sum_intserial(x), x))
print('\n'.join(seriallist))
