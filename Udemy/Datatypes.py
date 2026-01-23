# Day 2 - 100 Days of Code

# Tip Calculator
print(f"\n---- Welcome to Tip Calculator! ----")

hang_out = float(input("\nHow much was the total bill? $ : "))
tip_share = int(input("How much tip would you like to give? (10% , 12%  or 15%) : "))
total_peeps = int(input("How many people would be on the split? : "))

individual_share = round(((hang_out * tip_share / 100) + hang_out) / total_peeps, 2)

print(f"\n____ Each person share : ${individual_share} ! ____")