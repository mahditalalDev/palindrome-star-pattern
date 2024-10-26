# Prompt the user to enter the number of rows for the diamond pattern
user_input = int(input("Please enter the number of rows: "))

# Initialize variables for the pattern output and initial spacing
output = 0
spacing = 0

# Loop to create each row of the diamond pattern
for i in range(user_input * 2 - 1):
    # For the top half of the diamond, including the middle row
    if i < user_input:
        if i == 0:
            # Set initial spacing and print the first row with a single star
            spacing = user_input - 1
            print(" " * spacing, "*")
            output = 1  # Initialize output to control star count
        else:
            # Increase stars by 2 for each row and decrease spacing by 1
            output += 2
            spacing -= 1
            print(" " * spacing, "*" * output)
    else:
        # For the bottom half of the diamond
        # Decrease stars by 2 and increase spacing by 1 for each row
        output -= 2
        spacing += 1
        print(" " * spacing, "*" * output)
