# -*- coding: utf-8 -*-
# 문제 2. matplotlib을 활용하여 각 단어의 출현 횟수 순위(x축) 와 각 단어의 출현 횟수 (y축)를 log scale에서 출력하고, 지프의 법칙을 따르는지 확인하기
__author__ = 'JudePark'
__email__ = 'judepark@kookmin.ac.kr'
__repository__ = 'https://github.com/JudePark96/2020-datascience-kmu-wordcount'


import matplotlib.pyplot as plt
import math
import sys


#freqs = [int(line.split('\t')[1].strip()) for line in sys.stdin]
freqs = list(map(lambda x: int(x.split('\t')[1].strip()), sys.stdin))
n = 1000
ranks = range(1, n+1)

# 그래프 그리기
plt.plot(ranks, freqs)
plt.xlabel('log(rank)')
plt.ylabel('log(freq)')
plt.yscale('log')
plt.xscale('log')
plt.savefig('./result.png')
# plt.show() 서버에서 돌리면 안됨.

# $$ n = ck^{-s} $$
# y = freq, x = rank
# log 를 취함.
ys, xs = list(map(math.log, freqs)), list(map(math.log, ranks))
sxy, sx, sy = 0, 0, 0

length = len(xs)
ex = sum(xs) / length
ey = sum(ys) / length
for x, y in zip(xs, ys):
    nx = x - ex
    ny = y - ey
    sxy += nx * ny
    sx += nx * nx
    sy += ny * ny

s = sxy / sx
c = ey + s * ex


print('c = {}'.format(c))
print('s = {}'.format(s))
