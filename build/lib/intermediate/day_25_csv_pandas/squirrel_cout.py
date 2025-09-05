import pandas


def count_squirrels(file_path: str):
    data = pandas.read_csv(file_path)
    colors = data["Primary Fur Color"]
    colors_dict = {}

    # for color in colors:
    #     if color == 'Gray':
    #         colors_dict['Gray'] = colors_dict.get('Gray', 0) + 1
    #     elif color == 'Cinnamon':
    #         colors_dict['Cinnamon'] = colors_dict.get('Cinnamon', 0) + 1
    #     elif color == 'Black':
    #         colors_dict['Black'] = colors_dict.get('Black', 0) + 1
    #     elif color == 'NaN':
    #         colors_dict['_NaN'] = colors_dict.get('NaN', 0) + 1
    #     else:
    #         colors_dict[color] = colors_dict.get(color, 0) + 1
    for color in colors:
        colors_dict[color] = colors_dict.get(color, 0) + 1

    print(colors_dict)

    result = []
    for key, value in colors_dict.items():
        result.append(dict({'color': key, 'count': value}))

    print(result)

    colors_data_frame = pandas.DataFrame(result)
    colors_data_frame.to_csv('squirrel_colors_grouped.csv')

    # result_dict = {'color', 'count'}



if __name__ == "__main__":
    count_squirrels('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')