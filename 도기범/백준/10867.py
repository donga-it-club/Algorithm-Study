# -*- coding: utf-8 -*-
"""baekjoon_10867.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cF-MrfgqpenbVzhbUQhFan4pEE0_GVDZ
"""

ln = input()
ls = list(map(int,input().split()))
ls = list(set(ls))
ls.sort()
for i in ls:
    print(i,end = ' ')