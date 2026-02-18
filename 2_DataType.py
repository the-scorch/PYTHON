# Declaring Integer variable
adlt = 18
print(adlt)
adlt = 21 # updating variable
print(adlt, type(adlt)) # gives type of variable

# Float variable
a = -9.8
print(a, type(a))

# String variable
fname = "Code"
lname = "Chef"
print(fname, lname, type(fname))

# Bool variable
earth_round = True
water_red = False
print(earth_round, water_red, type(earth_round))

# Type Conversion
quot = 7
print(quot, type(quot))
quot = quot/2 # Implicit
print(quot, type(quot))

num = 61
print(num, type(num))
num = str(num) # Explicit to string
print(num + num, type(num))
num = bool(num) # Explicit to bool
print(num, type(num))
num = float(num) # Explicit to float
print(num, type(num))

print(int(5/2)) # truncates the Float 2.5 to Intger 2