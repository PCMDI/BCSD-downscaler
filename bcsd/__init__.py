import numpy as np


def qmap_fit(x, y, steps=0.01, axis=None):
    x_map = np.percentile(x, steps, axis=axis)
    y_map = np.percentile(y, steps, axis=axis)
    return x_map, y_map

def qmap_predict(x_map, y_map, y, axis=None):
    idx = [np.abs(val - y_map).argmin(axis=axis) for val in y]
    if axis == 0:
        return np.asarray([x_map[k, range(y.shape[1])] for k in idx])
    return x_map[idx]

