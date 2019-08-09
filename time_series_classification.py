# -*- coding:utf-8 -*-
# author : 囧囧有神
# data : 2019/08/09 14:21

import numpy as np
import matplotlib.pyplot as plt
from pyts.approximation import PiecewiseAggregateApproximation

n_samples, n_timestamps = 100, 48

rng = np.random.RandomState(41)
X = rng.randn(n_samples, n_timestamps)
print(X.shape)


