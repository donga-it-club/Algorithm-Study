# -*- coding: utf-8 -*-
"""baekjoon_10815.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-bCDYeaT0HQtC9U8t1TqANsgPiL7cdte
"""

num1= int(input())
inp = list(map(int,input().split()))
b = int(input())
tar = list(map(int,input().split()))
dic = {}
for i in inp:
    dic[i] = True
for i in tar:
    if i in dic:
        print(1,end=' ')
    else:
        print(0,end=' ')