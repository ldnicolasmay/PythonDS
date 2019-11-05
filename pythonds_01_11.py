# Python DS
# 1.11 Exception Handling

import math

# for i in range(10)

a_number = int(input("Please enter an integer: "))

print(math.sqrt(a_number))

try:
    print(math.sqrt(a_number))
except:
    print("Bad Value for square root")
    print("Using absolute value instead")
    print(math.sqrt(abs(a_number)))

if a_number < 0:
    raise RuntimeError("You can't use a negative number")
else:
    print(math.sqrt(a_number))

