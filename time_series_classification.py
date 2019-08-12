# -*- coding:utf-8 -*-
# author : 囧囧有神
# data : 2019/08/09 14:21

import numpy as np
import matplotlib.pyplot as plt
from pyts.approximation import PiecewiseAggregateApproximation
from pyts.utils import segmentation
import pandas as pd

# 1、近似算法
# 1.1 分段聚合近似
# pyts.approximation.PiecewiseAggregateApproximation
# PAA
n_samples, n_timestamps = 2, 10

rng = np.random.RandomState(41)
X = rng.randn(n_samples, n_timestamps)
print(X)

windows_size = 2
paa = PiecewiseAggregateApproximation(window_size=windows_size)
X_paa = paa.transform(X)
print(X_paa)

seg = segmentation(10, window_size=3, overlapping=False)
print(seg)

# 1.2 符号聚合近似 Symbolic Aggregate approXimation SAX

from pyts.approximation import SymbolicAggregateApproximation
X = [[0, 4, 2, 1, 7, 6, 3, 5], [2, 5, 4, 5, 3, 4, 2, 3]]
sax = SymbolicAggregateApproximation()
print(sax.transform(X))