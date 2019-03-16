"""
numpy 常见数学运算

ndarray.min() / np.min(ndarray) 最小值
ndarray.max() / np.max(ndarray) 最大值
ndarray.mean() / np.mean(ndarray) 平均值
ndarray.sum() / np.sum(ndarray) 求和
np.exp() 求幂
np.sqrt() 开方
np.sort() 排序
np.argsort() 按从小到大排序的元素的索引
"""

import numpy as np
n = np.array([[5,10,15],[20,25,30],[35,40,45]])
print(n.min()) #返回5 
print(np.min(n)) #返回5
print(n.max()) #返回45
print(np.max(n)) #返回45
print(n.mean()) #返回25.0(
print(np.mean(n)) #返回25.0
print(n.sum())  #返回225
print(np.sum(n)) #返回225

print("-" * 20)
#以上所有方法都可以指定所操作的维度，axis=0 按列，axis=1 按行按行，如
print(n.sum(axis=1)) #返回[ 30  75 120]
print(np.sum(n,axis=0)) #返回[60 75 90]

print("-" * 20)
print(np.exp(n))
"""
[[1.48413159e+02 2.20264658e+04 3.26901737e+06]
 [4.85165195e+08 7.20048993e+10 1.06864746e+13]
 [1.58601345e+15 2.35385267e+17 3.49342711e+19]]
 """
print(np.sqrt(n))
"""
[[2.23606798 3.16227766 3.87298335]
 [4.47213595 5.         5.47722558]
 [5.91607978 6.32455532 6.70820393]]
"""
print("-" * 20)
a = np.array([[4,3,5],[1,6,1]])
print(np.sort(a)) #只能用该方法，不能用方法a.sort()

print(np.argsort(a))
"""
[[1 0 2]
 [0 2 1]]
 """