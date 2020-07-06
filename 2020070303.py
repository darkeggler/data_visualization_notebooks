# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 14:42:48 2020

@author: deg
"""


import matplotlib.pyplot as plt

from matplotlib.patheffects import withStroke
from matplotlib.path import Path
from matplotlib.transforms import Affine2D, IdentityTransform
from matplotlib.collections import PathCollection
from matplotlib.markers import MarkerStyle

import numpy as np

%matplotlib widget

px = np.random.rand(10)
py = np.random.rand(10)

offsets = np.ma.column_stack([px, py])

#%% 1
fig, ax = plt.subplots()

reduction = 50
c = Path.unit_circle()
c = c.transformed(Affine2D().scale(0.5 * reduction))

collection = PathCollection(
    (c,), offsets=offsets, 
    transOffset = ax.transData,
    edgecolor='black', 
    facecolor=(0, 0, 0, .0125),
    linewidth=1
)

collection.set_transform(IdentityTransform())
ax.add_collection( collection )

#%% 2

collection.set_path_effects([withStroke(linewidth=5, foreground='r')])
collection.set_path_effects([])
collection.get_path_effects()


