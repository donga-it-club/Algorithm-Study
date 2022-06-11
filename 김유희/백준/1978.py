import sys

N = sys.stdin.readline()
numbers = list(map(int, input().split()))

def isPrime(numberlist):
    count = 0
    for i in numberlist:
        if i <= 1:
            continue
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            count += 1

    return count

print(isPrime(numbers))
