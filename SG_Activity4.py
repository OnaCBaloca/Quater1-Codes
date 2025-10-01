# Ask the user to input their full name
full_name = input("Enter your full name (First, Middle, Last): ")

# Split the input by commas
names = full_name.split(',')

# Extract first, middle, and last names
first = names[0].strip().capitalize()
middle = names[1].strip().capitalize()
last = names[2].strip().title()  # Handles multi-word last names like "dela cruz"

# Get the middle initial
middle_initial = middle[0] + "."

# Format the final name
formatted_name = f"{last}, {first} {middle_initial}"

# Display the result
print("Formatted Name:", formatted_name)



