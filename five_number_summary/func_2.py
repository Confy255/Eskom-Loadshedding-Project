import numpy as np
import pandas as pd

ebp_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/electrification_by_province.csv'
ebp_df = pd.read_csv(ebp_url)

for col, row in ebp_df.iloc[:,1:].iteritems():
    ebp_df[col] = ebp_df[col].str.replace(',','').astype(int)

ebp_df.head()

"""THIS FUNCTION WORKS AS SUCH;
        >Takes in a list of integers
        >Returns a dictionary with the five number summarry (median, q1, q3, max, min) 
         as keys and corrisponding values,rounded to two decimal places, as values to the keys.
"""

### START FUNCTION
def five_num_summary(items):
    maximum = round(max(items),2)
    median = round(np.median(items),2)
    minimum = round(min(items),2)
    Q1 = round(np.percentile(items, 25), 2)
    Q3 = round(np.percentile(items, 75), 2)
    return {'max': maximum, 'median': median, 'min': minimum, "q1":Q1, "q3":Q3}
### END FUNCTION