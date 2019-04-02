#!/usr/bin/env python
# filename: plot.py

import itertools
import os
import sys

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from abutils.utils import mongodb
from abutils.utils import color

import pymongo

from natsort import natsorted

def df_freq_barplot(df, cols=None):

    #get the columns
    if not cols:
        cols = list(df.columns)

    #melt the df
    df = df.melt(id_vars='index', value_vars=cols)

    #plot
    sns.barplot(data = df, x='index', y='value', hue='variable')
    

