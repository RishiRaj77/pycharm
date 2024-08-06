import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240805.csv")
greysql_count = len(data[data["Primary Fur Color"] == "Gray"])
greysql_count1 = len(data[data["Primary Fur Color"] == "Cinnamon"])
greysql_count2 = len(data[data["Primary Fur Color"] == "Black"])


print(greysql_count)
print(greysql_count1)
print(greysql_count2)

data_dict = {
     "fur color" : [ "Gray" , "Cinnamon", "Black"],
    "count ": [ greysql_count ,greysql_count1 ,greysql_count2]
}

df = pandas.DataFrame(data_dict)
df.to_csv("newfile.csv")
