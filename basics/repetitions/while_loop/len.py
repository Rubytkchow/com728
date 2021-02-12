print("Please enter a phrase.")
phrase = input()

bop = 0
print()

while bop < len(phrase):
    print("bop ", end="")
    bop = bop + 1

userInput = (input("Please enter a phrase:\n"))
#print(f"{'bop ' * userInput}")

# The while loop way

i = 0

while i < len(userInput):
    print("bop", end="")
    i = i + 1