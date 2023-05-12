import os
import pandas as pd
import torch

data_file1 = os.path.join('..', 'data', 'house_tiny.csv')
data = pd.read_csv(data_file1)

#select columns either by name or via integer-location based indexing (iloc).
inputs, targets = data.iloc[:, 0:2], data.iloc[:, 2]
print(inputs)
print(targets)

inputs = pd.get_dummies(inputs, dummy_na=True)
print(inputs)

#replace the NaN entries with the mean value of the corresponding column.
inputs = inputs.fillna(inputs.mean())
print(inputs)
