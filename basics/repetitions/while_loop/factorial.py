print("Please enter a number.")
fact_num = int(input())

count = 0
total = 1

while count < fact_num:
    count = count + 1
    total = total * count
#indented means runs inside the loop so it will print it multipletimes,
    # but not indented means it will print once
    #print(f"The factorial is {total}.")
print(f"The factorial is {total}.")
