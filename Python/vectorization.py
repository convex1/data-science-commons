import pandas as pd
import numpy as np

#create dummy dataframe about dragon ball z characters earth location and other information

data = {"name": ["goku", "gohan"], "city": ["NY", "SEA"]}
dragon_ball_on_earth = pd.DataFrame(data=data)

#create new series (column) by using vectorization
dragon_ball_on_earth['is_goku'] = np.where(dragon_ball_on_earth['name'] == "goku", 1, 0)