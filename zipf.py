# -*- coding: utf-8 -*-
# 문제 2. matplotlib을 활용하여 각 단어의 출현 횟수 순위(x축) 와 각 단어의 출현 횟수 (y축)를 log scale에서 출력하고, 지프의 법칙을 따르는지 확인하기
__author__ = 'JudePark'
__email__ = 'judepark@kookmin.ac.kr'
__repository__ = 'https://github.com/JudePark96/2020-datascience-kmu-wordcount'


import matplotlib.pyplot as plt
import math
import sys
import numpy as np

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
plt.savefig('./h01_박은환_20163108.png')


freqs = np.log(freqs)
ranks = np.log([i for i in ranks])

del_x = ranks[-1] - ranks[0]
del_y = freqs[-1] - freqs[0]

s = (del_y / del_x) * -1
c = np.exp(freqs + s * ranks)

sum_c = 0

for i in range(1, 1000):
    sum_c += c[i]

aprox_c = sum_c / 1000

print(f"s: {s}")
print(f"c: {aprox_c}")



# plt.show() 서버에서 돌리면 안됨.


# $$ n = ck^{-s} $$
# y = freq, x = rank
