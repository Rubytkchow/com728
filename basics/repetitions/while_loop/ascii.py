print("How many bars should be charged?")
uncharged_bars = int(input())

charged_bars = 0

print()

while charged_bars < uncharged_bars:
    charged_bars = charged_bars +1
    print(f"charging {'█' * charged_bars}")

print("The battery is fully charged.")