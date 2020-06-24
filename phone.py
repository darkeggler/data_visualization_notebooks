# -*- coding: utf-8 -*-
"""
Spyder Editor

京东手机TOP10数据分析.

问题列表：
%matplotlib widget在这里如何使用？或者说Spyder中如何便利的使用matplotlib
"""

# Part I. 基础图表

import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes, mark_inset

import pandas as pd
import numpy as np

matplotlib.rcParams['font.family'] = ['DengXian', 'sans-serif']
matplotlib.rcParams['axes.unicode_minus'] = False
plt.ion()
#%%1.数据准备
"""markdown
基础图表1 - 长宽比例图

每一条折线表示一款手机，其有三个顶点，左下原点，屏幕右上点，手机右上点。
屏幕尺寸的计算方法：

    > $\frac{\sqrt{x^2+y^2}}{Z}$
计算对角线的像素数除以对角线长度算出PPI，之后计算屏幕长与宽。

"""
fn = r'D:\notebooks\data_visualization_notebooks\phone_data2.csv'
df = pd.read_csv(fn).iloc[0:15]
row, col = df.shape
c = df['CPU'].astype('category')
ec = list(enumerate(c.cat.categories))

ppi = np.sqrt(df['分辨率宽']**2 + df['分辨率长']**2) / (df['屏'] * 25.4)

x1 = df['宽']
y1 = df['长']

x2 = df['分辨率宽'] / ppi
y2 = df['分辨率长'] / ppi

px = list(zip([0]*15, x2, x1))
py = list(zip([0]*15, y2, y1))

#%%2.尺寸图
fig = plt.figure(figsize=(5,5))

ax = fig.add_subplot(121)
ax.set_aspect(1)

for i in range(15):
    ax.plot(px[i], py[i], lw=0.35, marker='o', alpha=0.75)

axins = zoomed_inset_axes(ax, 4, loc=2, borderpad=0,
                          bbox_to_anchor = (1.2, .3, .8, .7),
                          bbox_transform = ax.transAxes
                         )

for i in range(15):
    axins.plot(px[i], py[i], lw=0.35, marker='o', alpha=0.75)

#ax.set_aspect(1)
axins.set_xlim(65, 80)
axins.set_ylim(145, 165)

mark_inset(ax, axins, loc1=2, loc2=2, fc="none", ec="0.5")

#%%3.
"""
横坐标怎样添加偏置？

heft  重量
"""
fig2, ax2 = plt.subplots(figsize=(3,5))

heft_df = df.sort_values(by = '重')
heft_df.index = np.arange(row)

for n, r in ec:
    tdf = heft_df[heft_df['CPU'] == r]
    ax2.barh(tdf.index, tdf['重'] - 180, 
                    color='C%d' % n,
                    height=0.7
                   )

ax2.set_yticks(heft_df.index.values)
ax2.set_yticklabels(heft_df['name'])
ax2.set_xticklabels(['140','160','180','200','220'])

