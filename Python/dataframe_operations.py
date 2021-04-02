import pandas as pd
import numpy as np

"""
create dummy dataframe about dragon ball z characters earth location and other information
"""

name_data_one = {"name": ["goku", "gohan"], "power": [200, 400], city": ["NY", "SEA"]}
name_data_two = {"name": ["srijan", "chuck"], "power": [400, 500], city": ["DEN", "SFO"]}
dragon_ball_data_one = pd.DataFrame(data=name_data_one)
dragon_ball__data_two = pd.DataFrame(data=name_data_two)

"""
Concatenate two dataframes

"""

pd.concatenate([name_data_one, name_data_two], axis=0) #concatenate along rows - stack vertically

pd.concatenate([name_data_one, name_data_two], axis=1) #concatenate along column - stack horizontally


"""
Join/Merge two dataframes

"""

pd.merge(name_data_one, name_data_two, on = "name", how="inner")


"""
Loop over dataframes

"""

#using itterows()
#following will iterate over and print each index and name column for that rows in that index
for index, row in name_data_one.iterows():
    print(index, row["name"])

#using iteritems()
#following will iterate over and print each column and full column series
for column_name, column_series in name_data_one.iteritems():
    print(column_name, column_series)