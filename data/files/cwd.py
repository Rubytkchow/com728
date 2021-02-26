# We wish to create a program to display information about the current working directory.
#
# The program should consist of the following two functions:
#
# The first function should be named cwd and should have no parameters.
# The function should retrieve the file path for the current working folder.
# The function should then display the message "The current working directory is {path}" where {path} is the previously retrieved path.
# The function should then display the message "The directory contains the following files:".
# Finally, the function should display each file contained in the current working directory.
# The second function should be named run and should have no parameters.
# The function should display the message "Processing...".
# The function should then call the first function.

import os
def cwd():
    path = os.getcwd()
    print(f"The current working directory is {path}")

    for file in os.listdir(path):
        print("The directory contains the following files:", file)

def run():
    print("Processing...")
    cwd()

run()