# Ronald Woods
# CSD325 - T301
# 12/03/2025
# A program that prints the "99 Bottles of Beer"


# Ask the user for a number
try:
    n = int(input("How many bottles of beer are on the wall? "))
except ValueError:
    print("Please enter a whole number next time.")
    quit()

# Loop until we get to 0
while n > 0:
    print(n, "bottles of beer on the wall,", n, "bottles of beer.")

    # Take one down
    n = n - 1

    if n > 0:
        print("Take one down and pass it around,", n, "bottles of beer on the wall.")
    else:
        print("Take one down and pass it around, no more bottles of beer on the wall.")

    print()  # Just a blank line

# Ending lines
print("No more bottles of beer on the wall, no more bottles of beer.")
print("Go to the store and buy some more!")
