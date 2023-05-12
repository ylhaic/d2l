import os
import pandas as pd
import torch

data_file = os.path.join('..', 'data', 'house_tiny.csv')
data = pd.read_csv(data_file)

inputs, targets = data.iloc[:, 0:2], data.iloc[:,2]
inputs = pd.get_dummies(inputs, dummy_na=1)
inputs = inputs.fillna(inputs.mean())

X, y = torch.tensor(inputs.values), torch.tensor(targets.values)
print(X)
print(y)