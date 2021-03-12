import json

def read(file_path):
    with open(file_path) as file:
        data = json.load(file)

        #display the name of the city
        city_name = data["city"]
        print(f"City name: {city_name}")

        #display the population size
        population = data["population"]
        print(f"Population size: {population}")

        #displaythe message "{name} has the following stats: {stats}" where {name} and {stats}are the name and stats of the bot.
        for bot in data["bots"]:
            name = bot["name"]
            stats = bot["stats"]
            print(f"{name} has the following stats: {stats}")

def run():
    read("robocity.json")

if __name__ == "__main__":
    run()