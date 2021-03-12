def pattern():
    sequences = {"Short Sequence":3, "Medium Sequence":2, "Long Sequence":1}
    return sequences

def display_keys(data):
    for key in data.keys():
        print(f"{key}")
    print()

def display_values(data):
    for value in data.values():
        print(f"{value}")
    print()

def display_items(data):
    for key, value in data.items():
        print(f"{key}: {value}")
    print()

def run():
    data = pattern()
    print(f"Dictionary: \n {data}")

    display_keys(data)
    display_values(data)
    display_items(data)

if __name__ == "__main__":
    run()

