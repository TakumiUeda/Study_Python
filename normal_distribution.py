#coding: UTF-8
from scipy import stats
from numpy.random import *
import matplotlib.pyplot as plt
NUM=10000;
# 描画範囲の指定

r = randn(NUM)

# 横軸の変数。縦軸の変数。
plt.hist(r, bins=100)

# 描画実行
plt.show()
