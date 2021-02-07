import pandas as pd
import numpy as np

"""
~~ABOUT~~
Use vectorization instead of using for loops to assign new values. Try to do it whenever possible.
It will be possible in most cases except a few minor comlicated cases where for loop might be required.None
"""


"""
create dummy dataframe about dragon ball z characters earth location and other information
"""

data = {"name": ["goku", "gohan"], "city": ["NY", "SEA"]}
dragon_ball_on_earth = pd.DataFrame(data=data)

"""
create new series (column) by using vectorization
there is one single condition and one single outcome except the default
"""

dragon_ball_on_earth['is_goku'] = np.where(dragon_ball_on_earth['name'] == "goku", 1, 0)


"""
How to assign the series column based on multiple conditions?

Use np.select() instead of np.where()
np.select() can take multiple conditions and multiple outcomes

"""

conditions =[[dragon_ball_on_earth['name'] == "goku"], [dragon_ball_on_earth['name'] == "gohan"]]
outcomes = [1,2]

dragon_ball_on_earth['coded_name'] = np.select(conditions, 1, 0)