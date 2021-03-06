# -*- coding: utf-8 -*-
"""baekjoon_16401.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Z2BJ3rFc2XJVrBNVc1I8IsYQaPxohpmg
"""

import sys
input = sys.stdin.readline
pn, sn = map(int, input().split())
ls = list(map(int,input().split()))
left = 1 # 0으로 시작하면 zerodevisionError 발생
right = max(ls)
while left <= right:
    count = 0
    mid = (left + right)//2
    for k in ls:
        if k >= mid:
            count += k//mid
    if count >= pn:
        left = mid + 1
    elif count < pn:
        right = mid - 1
print(right)