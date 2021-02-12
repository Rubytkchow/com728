print("how many numbers should I sum up?")
sum_num = int(input())

cal_num = 0

print()

sum = 1

while sum <= sum_num:
    print(f"Please enter number {sum} of {sum_num}")
    sum = sum + 1
    cal_num = int(input()) + cal_num

print(f"The answer is {cal_num}")

# Ask user for number
print("How many numbers should I sum up?")
number_to_sum = int(input())

# Declare a control variable
summed = 0

# Display blank line
print()

# Sum numbers
total = 0

while summed < number_to_sum:
    print(f"Please enter number {summed} of {number_to_sum}:")
    number = int(input())
    total = total + number
    summed = summed + 1

# Display result
print(f"The answer is {total}.")






userAmount = int(input("How many numbers should I sum up?\n"))
i = 1
total = 0
while i <= userAmount:
    print(f"Please enter number {i} of {userAmount}")
    total = int(input()) + total
    i = i + 1
print(f"The total is {total}.")