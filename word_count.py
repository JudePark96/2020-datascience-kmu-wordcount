# -*- coding: utf-8 -*-
# 문제 1. 문서를 입력받아 자주 등장하는 단어 1000개를 자주 등장하는 순서대로 출력하는 python 프로그램 작성하기
__author__ = 'JudePark'
__email__ = 'judepark@kookmin.ac.kr'
__repository__ = 'https://github.com/JudePark96/2020-datascience-kmu-wordcount'

import logging
import re
import sys

from collections import defaultdict

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s -   %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

vocab = defaultdict(int)

for idx, line in enumerate(sys.stdin):
    # 영어 및 일부 특수 문자만 존재하도록
    line = re.sub(r'[^\x00-\x7F]+', '', line.strip().lower())
    # 길동 is one of Tom’s best friends. -> [‘is’, ‘one’, ‘of’, ‘tom’, ‘s’, ‘best’, ‘friends’] 로 . 이 빠져있다.
    # . 을 지우도록...
    line = re.sub(r'[_<>,\(\)\.\'%]', '', line).split(' ')

    for word in line:
        # defaultdict 이기 때문에 exception 생각안해도 됨.
        if word in vocab:
            vocab[word] += 1
        else:
            vocab[word] = 1

    if idx % 100000 == 0:
        logger.info(f'loop index: {idx}')
        logger.info(f'vocabulary size: {len(vocab)}')

k = 1000
top_k = sorted(vocab, key=vocab.get, reverse=True)[:k]

for item in top_k:
    print(f'{item}\t{vocab[item]}')
