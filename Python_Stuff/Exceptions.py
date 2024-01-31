import sys

x = int(input("X: "))
y = int(input("Y: "))

try:
    result = x / y
except ZeroDivisionError:
    print(f"ERROR: You cannot divide by 0!")
    sys.exit(1)

print(f"{x} / {y} = {result}")

