import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
def drop_numerical_outliers(df, z_thresh=3):
    constrains = df.select_dtypes(include=[np.number]).apply(lambda x: np.abs(stats.zscore(x)) < z_thresh) \
        .all(axis=1)
    df.drop(df.index[~constrains], inplace=True)
    
def forest_feature_importance(df,title ):
    fig, ax = plt.subplots(figsize=(16, 9))
    df.plot.barh(ax=ax)
    ax.set_title(title)
