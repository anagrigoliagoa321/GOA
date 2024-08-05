def calculate_product(numbers):
    product = 1
    for number in numbers:
        product *= number
    print(product)


calculate_product([1, 2, 3, 4])  

def remove_negative_numbers(numbers):
    new_list = [num for num in numbers if num >= 0]
    print(new_list)


remove_negative_numbers([1, -2, 3, -4, 5]) 

def find_mean(numbers):
    if len(numbers) == 0:
        return None  
    mean = sum(numbers) / len(numbers)
    return mean


print(find_mean([1, 2, 3, 4]))  

def concatenate_lists(list1, list2):
    combined_list = list1 + list2
    print(combined_list)


concatenate_lists([1, 2, 3], [4, 5, 6])  



def duplicate_list(numbers):
    duplicated_list = numbers * 2
    print(duplicated_list)

duplicate_list([1, 2, 3])  