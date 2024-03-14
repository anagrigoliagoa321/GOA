
# Create a list of 10 integers
numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Iterate through the list and perform operations
for num in numbers:
    # Multiply
    result_multiply = num * 2
    print(f"Multiplying {num} by 2 equals {result_multiply}")
    
    # Divide
    result_divide = num / 2
    print(f"Dividing {num} by 2 equals {result_divide}")
    
    # Add
    result_add = num + 5
    print(f"Adding 5 to {num} equals {result_add}")
    
    # Subtract
    result_subtract = num - 5
    print(f"Subtracting 5 from {num} equals {result_subtract}")

# Create a list
values = [1, 2, 3, 4, 5]

# Extract and replace values
for index in range(len(values)):
    # Extracting value
    extracted_value = values.pop(0)
    print(f"Extracted value: {extracted_value}")

    # Replacing with another value
    values.append(extracted_value * 2)
    print("List after replacement:", values)

# Create a list
my_list = [10, 20, 30, 40, 50]

# Let the user choose a desired value
desired_value = int(input("Enter the desired value: "))

# Check if the desired value is in the list
if desired_value in my_list:
    print(f"{desired_value} is in the list.")
else:
    print(f"{desired_value} is not in the list.")

("Sentences with Provided Words:")
("The value of this item minus the value of that item is ten")
("The list contains a variety of fruits")
("Please enclose this expression in parentheses")
("Separate the elements with commas")
("Does the library include references to those articles")
("Access to the database requires permissio")
("The two solutions are different from each other")
("The output of the program is displayed on the screen")
("Lists are mutable, meaning they can be changed")
("Once assigned, the value of a constant is immutable")
("Would you like a lime or a lemon in your drink")
("The monitor will display the image in high definition")
("DNA and RNA are both types of sequences")
("Can you define the purpose of this function")