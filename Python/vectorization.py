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
"""

dragon_ball_on_earth['is_goku'] = np.where(dragon_ball_on_earth['name'] == "goku", 1, 0)