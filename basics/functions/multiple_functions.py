def display_ladder(steps):
    for step in range(steps):
        print("| |")
        print("***")
    print("| |")
def create_ladder():
    print("What is the number of steps?")
    steps = int(input())
    display_ladder(steps)

create_ladder()
