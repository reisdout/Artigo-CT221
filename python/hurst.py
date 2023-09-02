# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 18:14:14 2023

@author: visitante
"""

import numpy as np
import matplotlib.pyplot as plt
import hurst as ht  

# Use random_walk() function or generate a random walk series manually:
# series = random_walk(99999, cumprod=True)
np.random.seed(42)
random_changes = 1. + np.random.randn(99999) / 1000.
series = np.cumprod(random_changes)  # create a random walk from random changes

# Evaluate Hurst equation
H, c, data = (series, kind='price', simplified=True)

print("H={:.4f}, c={:.4f}".format(H,c))