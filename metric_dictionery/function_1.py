import numpy as np
def dictionary_of_metrics(items):
    mean = round(np.mean(items), 2)
    median = round(np.median(items), 2)
    var = round(np.var(items, ddof=1), 2)
    std_dev = round(np.std(items, ddof=1), 2)
    minimum = round(min(items), 2)
    maximum = round(max(items), 2)

    return {
        'mean': mean,
        'median': median,
        'var': var,
        'std': std_dev,
        'min': minimum,
        'max': maximum
        }
