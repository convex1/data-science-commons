import pandas as pd
import numpy as np


"""
Common filter values:
These are some common ways to filter your dataframe
"""

dragon_ball_on_earth[dragon_ball_on_earth['name'] == "goku"]
dragon_ball_on_earth[dragon_ball_on_earth['name'].isnull()]
dragon_ball_on_earth[dragon_ball_on_earth['name'].isna()]
dragon_ball_on_earth[dragon_ball_on_earth['name'] < "a"]


"""
~~ABOUT~~
Use vectorization instead of using for loops to assign new values. 
You can use them to filter values easily. Try to do it whenever possible.
It will be possible in most cases except a few minor complicated cases where for loop might be required.
Vector operation is better than Scala operations.
"""


"""
create dummy dataframe about dragon ball z characters earth location and other information
"""

data = {"name": ["goku", "gohan"], "power": [200, 400], city": ["NY", "SEA"]}
dragon_ball_on_earth = pd.DataFrame(data=data)

"""
create new series (column) by using vectorization
there is one single condition and one single outcome except the default
"""

dragon_ball_on_earth['is_goku'] = np.where(dragon_ball_on_earth['name'] == "goku", 1, 0)

characters_with_power_100_or_more = np.where((dragon_ball_on_earth['name'].notnull()) & (dragon_ball_on_earth['power'] > 100), 1, 0)

#you can also just get the indices of the rows that satisfy your condition
dataframe_indices = np.where(dragon_ball_on_earth['name'] == "goku")


"""
How to assign the series column based on multiple conditions?

Use np.select() instead of np.where()
np.select() can take multiple conditions and multiple outcomes

"""

conditions =[[dragon_ball_on_earth['name'] == "goku"],
             [dragon_ball_on_earth['name'] == "gohan"],
             [dragon_ball_on_earth['power_level'].isin([100, 200, 400])]]

outcomes = [1,2]

#conditions and outcomes are from the assigned variables above
#zero below is the default value to be assigned in case the conditions are not satisfied
dragon_ball_on_earth['coded_name'] = np.select(conditions, outcomes, 0)

