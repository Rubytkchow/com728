
def display_box(word):
    box_top = (len(word) + 3) * '*'
    print(box_top)
    print(f"* {word} *")
    print(box_top)

#display_box(word)


def display_low_case(word):
    print(word.lower())

def display_up_case(word):
    print(word.upper())

#display_up_case(word)

def display_mirrored(word):
    mirrored_word = ""
    for count in reversed(word):
        mirrored_word = mirrored_word + count
    print(mirrored_word)


#display_mirrored(word)

def repeat_word(word):
    times_repeated = int(input("How many repetitions of the word?\n"))
    for i in range(times_repeated):
        print(f"{word.lower()} {word.upper()}", end=" ")

#repeat_word(word)

def run():
    print("Enter a word")
    word = input()
    print("Choose one of the options")
    print("""
    1) Display in a Box – display the word in an ascii art box
    2) Display Lower-case – display the word in lower-case e.g. hello
    3) Display Upper-case – display the word in upper-case e.g. HELLO
    4) Display Mirrored – display the word with its mirrored word e.g. Hello | olleH
    5) Repeat – ask the user how many times to display the word and then display the word that 
       many times alternating between upper-case and lower-case.""")
    user_selection = int(input())
    if user_selection == 1:
        display_box(word)
    elif user_selection == 2:
        display_low_case(word)
    elif user_selection == 3:
        display_up_case(word)
    elif user_selection == 4:
        display_mirrored(word)
    elif user_selection == 5:
        repeat_word(word)

run()