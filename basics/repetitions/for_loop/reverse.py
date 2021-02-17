print("What phrase do you see?")
phrase = input()

print()

print("Reversing...")
print("The phrase is:")
for position in range(len(phrase) - 1, -1, -1):
        print(phrase[position], end="")