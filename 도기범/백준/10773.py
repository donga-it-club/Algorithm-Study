# -*- coding: utf-8 -*-
"""baekjoon_10773.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sWaOv6MajuQO3q5DzM6RonL1yFGrZwcJ
"""

rep = int(input())
ls = []
sum = 0
for _ in range(rep):
    inp = int(input())
    if inp == 0:
        if len(ls) != 0:
            x = ls.pop()
            sum -= x
    else:
        ls.append(inp)
        sum += inp
print(sum)