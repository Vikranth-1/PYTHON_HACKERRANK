import math

# Read inputs
a = int(input())
b = int(input())

# Calculate angle in radians
angle_rad = math.atan(a / b)

# Convert to degrees
angle_deg = math.degrees(angle_rad)

# Round to nearest integer
result = round(angle_deg)

# Print with degree symbol using Unicode code point
print(f"{result}\u00b0")
