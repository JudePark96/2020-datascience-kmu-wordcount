# -*- coding: utf-8 -*-
# 문제 2. matplotlib을 활용하여 각 단어의 출현 횟수 순위(x축) 와 각 단어의 출현 횟수 (y축)를 log scale에서 출력하고, 지프의 법칙을 따르는지 확인하기
__author__ = 'JudePark'
__email__ = 'judepark@kookmin.ac.kr'
__repository__ = 'https://github.com/JudePark96/2020-datascience-kmu-wordcount'


import matplotlib.pyplot as plt
import sys

freqs = [int(line.split('\t')[1].strip()) for line in sys.stdin]
n = 1000
ranks = range(1, n+1)
plt.plot(ranks, freqs)
plt.xlabel('log(rank)')
plt.ylabel('log(freq)')
plt.yscale('log')
plt.xscale('log')
plt.savefig('./result.png')
# plt.show() 서버에서 돌리면 안됨.
# TODO => 지프 법칙 따르는지 확인하기.
