# Electricity Bill Calculator Program

import sys

# If units are provided as command-line argument
if len(sys.argv) == 2:
    units = float(sys.argv[1])
    print("User provided units")
else:
    # Default units
    units = 100
    print("Default units used")

# Rate per unit
rate = 5

# Calculate bill
bill = units * rate

print("Units Consumed:", units)
print("Electricity Bill (₹):", bill)

