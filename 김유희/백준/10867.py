import sys
input = sys.stdin.readline
input()
print(' '.join(map(str, sorted(list(set(map(int,input().split())))))))
#print(' ', join(*sorted({*input().split()}, key = int))
