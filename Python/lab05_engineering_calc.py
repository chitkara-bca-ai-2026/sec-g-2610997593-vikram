import math

# Print Header
print("=========================================")
print("      ENGINEERING CALCULATION TOOL       ")
print("=========================================")


val = float(input("Enter a numerical value: "))


exponent = float(input("Enter an exponent: "))


decimal_val = float(input("Enter a decimal measurement: "))


power_result = math.pow(val, exponent)

sqrt_result = math.sqrt(val)


ceil_result = math.ceil(decimal_val)
floor_result = math.floor(decimal_val)

print("\n--- Results ---")
print(f"{'Value':<20} : {val}")
print(f"{'Exponent':<20} : {exponent}")
print(f"{'Power (pow)':<20} : {power_result}")
print(f"{'Square Root (sqrt)':<20} : {sqrt_result:.4f}")
print(f"{'Decimal Value':<20} : {decimal_val}")
print(f"{'Ceil Value':<20} : {ceil_result}")
print(f"{'Floor Value':<20} : {floor_result}")
print("=========================================")