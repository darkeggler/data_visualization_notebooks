# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 17:24:01 2020

@author: gu
"""


import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1,2,3,4],[2,3,4,1])
fig.savefig(r"E:\notebooks\png\test.svg", format="svg")
