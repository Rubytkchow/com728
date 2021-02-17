print("How far are we from the cave?")
steps = int(input())
distance = steps
print()

for count in range(steps):
    print(distance, "steps remaining")
    distance = distance -1
print("We have reached the cave!")


