def sum_weight(bop_weight, beep_weight):
    total_weight = (bop_weight + beep_weight)
    return total_weight

def calc_avg_weight(bop_weight, beep_weight):
    avg_weight = sum_weight(bop_weight, beep_weight)/2
    return avg_weight

def run():
    print("What is the weight of Beep?")
    beep_weight = int(input())
    print("What is the weight of Bop?")
    bop_weight = int(input())
    print("What would you like to calculate (sum or average?)")
    sum_or_average = input()
    if sum_or_average == "sum":
        #(sum_weight)
        print(f"The sum of Beep and Bop's weight is {sum_weight(bop_weight, beep_weight)}.")
    elif sum_or_average == "average":
        #(calc_avg_weight)
        print(f"The average of Beep and Bop's weight is {calc_avg_weight(bop_weight, beep_weight)}.")

run()


