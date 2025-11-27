import sys
if len(sys.argv) == 2:
    units = float(sys.argv[1])
    print("User provided units")
else:
    units = 100
    print("Default units used")
rate = 5
bill = units * rate

print("Units Consumed:", units)
print("Electricity Bill (₹):", bill)
