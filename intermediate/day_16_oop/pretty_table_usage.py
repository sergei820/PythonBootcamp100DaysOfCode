from prettytable import PrettyTable


def run_app():
    table = PrettyTable()
    table.add_column("Pokemon", ["Picachu", "Squirtle", "Charmander"])
    table.add_column("Type", ["Electric", "Water", "Fire"])
    table.align = "l"
    print(table)


if __name__ == '__main__':
    run_app()
