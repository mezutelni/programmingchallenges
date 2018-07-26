import sys
import math
temp = input("What's temperature you want to convert?: ")
try:
    temp = int(temp)
except:
    print("This is not an int!")
    sys.exit()
unit = input("What's your temperature unit? (f/k/c): ")
k = c = f = float(0)

if unit.lower() == "k":
    f = temp * 9/5 - 459.67
    c = temp - 273.15
    k = temp
elif unit.lower() == "f":
    k = (temp+ 459.67) *5/9
    c = (temp - 32) *5/9
    f = temp
elif unit.lower() == "c":
    k = temp + 273.15
    f = temp * 9/5 + 32
    c = temp

print("K = %g \nF = %g \nC = %g" %(k,f,c))