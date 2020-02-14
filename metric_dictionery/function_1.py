import numpy as numpy
### START FUNCTION
def dictionary_of_metrics(items):
    mean = round(np.mean(items), 2)
    median = round(np.median(items), 2)
    variance = round(np.var(items, ddof=1),2)
    standard_deviation = round(np.std(items, ddof=1), 2)
    minimum = round(min(items), 2)
    maximum = round(max(items), 2)
     
    return {"mean": mean, "median": median, "var": variance,
            "std": standard_deviation, "min": minimum, "max":maximum}
