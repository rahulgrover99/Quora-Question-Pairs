#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 21:18:41 2019

@author: diksha
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import gc
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame

data = pd.read_csv("/home/diksha/Downloads/quora_duplicate_questions.tsv", sep="\t")


data.groupby('is_duplicate')['id'].count().plot.bar()

print("Total number of question pairs for training:")
print((len(data)))

print('Duplicate pairs(%):')
print(round(data['is_duplicate'].mean()*100, 2))


qids = pd.Series(list(data['qid1'])+list(data['qid2']) )
print('Total number of question in data set:')
print(len(np.unique(qids)))
print('Number of questions that appear multiple times:')
print(np.sum(qids.value_counts()>1))

plt.hist(qids.value_counts(), bins=50)
plt.yscale('log', nonposy='clip')
plt.title('Log-Histogram of question appearance counts')
plt.xlabel('Number of occurences of question')
plt.ylabel('Number of questions')
plt.show()
