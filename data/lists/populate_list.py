def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions

def menu():
    print("Please select a direction:")
    direct = directions()
    for index in range(len(direct)):
        print(f"{index}: {direct[index]}")
    index = int(input())
    return direct[index]

def run():
    route = []
    print("Working out escape route...")
    for count in range(0, 5, 1):
        route.append(menu())
    print(f"Escape route: {route}")

run()