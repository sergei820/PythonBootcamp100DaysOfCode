def parse_csv(filename: str):
    lines_list = []
    with open(filename, 'r') as file:
        lines_list = file.readlines()

    return lines_list

if __name__ == "__main__":
    print(parse_csv("./weather_data.csv"))
