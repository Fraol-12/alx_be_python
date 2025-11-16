# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop to handle rows (while loop)
while row < size:
    # Inner loop to handle columns (for loop)
    for col in range(size):
        print("*", end="")  # Print asterisk without newline
    print()  # Move to the next line after printing one row
    row += 1  # Increment row counter
