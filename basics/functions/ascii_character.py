print("Program started!")
print("Please enter an ASCII code:")
ASCII_code = int(input())

if ASCII_code in range(32,126):
    print(f"The character represented by the ASCII code {ASCII_code} is: {chr(ASCII_code)}.")

print("Program Ended!")
