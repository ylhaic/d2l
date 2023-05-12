import os
#CSV: comma-separated values
#create a CSV file below ../data/house_tiny.csv
#This file represents a dataset of homes
#where each row corresponds to a distinct home
#and the columns correspond to the number of rooms (NumRooms)
#the roof type (RoofType)and the price (Price).
os.makedirs(os.path.join('..', 'data'), exist_ok=True)
data_file1 = os.path.join('..', 'data', 'house_tiny.csv')
data_file2 = os.path.join('..', 'data', 'name.csv')
#write 'house_tiny.csv'
with open(data_file1, 'w') as f:
    f.write('''NumRooms,RoofType,Price
NA,NA,127500
2,NA,106000
4,Slate,178100
NA,NA,140000''')

import pandas as pd

data1 = pd.read_csv(data_file1)
#data2 = pd.read_csv(data_file2)
print(data1)
#print(data2)