print("Please enter a sequence")
sequence = input()

print("Please enter the character for the marker")
character = input()

character_position = -1
character_position2 = -1

for position in range(0, len(sequence), 1):
    letter = sequence[position]

    if letter == character:
        if (character_position == -1):
            character_position = position
        else:
            character_position2 = position

# Display result
print(f"The distance between the markers is {character_position2 - character_position - 1}.")
