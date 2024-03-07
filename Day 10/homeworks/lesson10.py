# Task 1: Create a list of programming languages
programming_languages = ["Python", "JavaScript", "Java", "C++", "Ruby"]
print(programming_languages)
print(programming_languages[-1])

# Task 2: Create a list with various data types
mixed_list = ["Hello", 42, 3.14, True]
str_element, int_element, float_element, bool_element = mixed_list
print(str_element)
print(int_element)
print(float_element)
print(bool_element)

# Task 3: Create a list of multiples of 4 from 0 to 20
multiples_of_4 = list(range(0, 21, 4))
print(max(multiples_of_4))

# Task 4: Create a list of odd numbers from 30 to 50
odd_numbers = list(range(31, 51, 2))
sum_of_smallest_3 = sum(sorted(odd_numbers)[:3])
print(sum_of_smallest_3)

# Task 5: Print multiples of three from the list in Task 4
multiples_of_three = [num for num in odd_numbers if num % 3 == 0]
print(multiples_of_three)