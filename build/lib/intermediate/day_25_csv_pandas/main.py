# import csv
#
# def parse_csv(file_path: str):
#     with open(file_path, 'r') as file:
#     #     data = file.readlines()
#         data = csv.reader(file)
#         temperatures = []
#         for row in data:
#             if row[1] != 'temp':
#                 temperatures.append(int(row[1]))
#     return temperatures

import pandas


def parse_csv(file_path: str):
    data = pandas.read_csv(file_path)
    # print(type(data))  # <class 'pandas.core.frame.DataFrame'> - equivalent to a table
    # temperatures = data["temp"]
    # print(type(temperatures))  # <class 'pandas.core.series.Series'> - equivalent to a column
    # print(temperatures[0])

    # data_dict = data.to_dict()
    # print(data_dict)

    # temp_list = data["temp"].to_list()
    # print(temp_list)

    # print(f"Avg value: {data["temp"].mean()}")
    #
    # print(f"Max value: {data["temp"].max()}")

    # Get data in Row
    # print(data[data.day == "Monday"])

    # Get the row with the highest temperature
    # print(data[data.temp == data["temp"].max()])

    monday = data[data.day == "Monday"]
    # print(monday.condition)
    print(f"Weather on Monday in ferenheit: {(monday.temp * 9/5) + 32}")

    # Create a dataframe from scratch
    data_dict = {
        "students": ["Amy", "James", "Angela"],
        "scores": [76, 56, 65]
    }
    data = pandas.DataFrame(data_dict)
    print(data)
    data.to_csv("new_csv.csv")

    result_dict = {'color', ''}

    # return temperatures


if __name__ == "__main__":
    # temperatures_list = parse_csv('./weather_data.csv')
    # print(temperatures_list)
    # print(sum(temperatures_list) / len(temperatures_list))
    parse_csv('./weather_data.csv')
