# -*- coding: utf-8 -*-
"""backjoon_2512.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1smfZNonIbY7_7EDJ7821SXY1buXKE9ON
"""

n = int(input())
ls = list(map(int,input().split()))
lim = int(input())
left = 1
right = max(ls)
while left <= right:
    sum = 0
    mid = (left + right)//2

    for k in ls:
        if k >= mid:
            sum += mid
        elif k < mid:
            sum += k
    if sum <= lim:
        left = mid + 1
    elif sum > lim:
        right = mid - 1
print(right)