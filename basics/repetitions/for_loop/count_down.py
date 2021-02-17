print("How far are we from the cave?")
steps = int(input())
distance = steps
print()

for count in range(steps):
    print(distance, "steps remaining")
    distance = distance -1
print("We have reached the cave!")

# Ask user for distance
print("How far are we from the cave?")
distance = int(input())

# Display count down
print()

for count in range(distance, 0, -1):
    print(f"{count} steps remaining")

print("We have reached the cave!")
