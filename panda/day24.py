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
# import pandas as pd
#
# data = pd.read_csv(" weather-data.csv ")
# print(data)

# import pandas
#
# # From a dictionary
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 35],
#     'City': ['New York', 'Los Angeles', 'Chicago']
# }
# df = pandas.DataFrame(data)
# print(df)

import pandas
# #
data = pandas.read_csv("weather-data.csv")
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list
# print(temp_list)
# (temp_list)
#
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["temp"].argmax())
#
#
# print(data["condition"])
# print(data.condition)
#
# print(data["temp"])
# print(data.temp)
# print(data["temp"].max())
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# print(data[data.condition == "Rain"])
print(data[data.temp == "Monday"])