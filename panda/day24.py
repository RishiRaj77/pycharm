# with open ( "weather-data.csv") as data_file:
#     data = data_file.readline()
#     print(data)
#
# import csv
#
# with open ( "weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature =[]
#     for row in data:
#         print(row)

#
# import panda as pd
#
# data = pd.read_csv(" weather-data.csv ")
# print(data)

import pandas

# From a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pandas.DataFrame(data)
print(df)


