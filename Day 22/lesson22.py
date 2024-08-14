#1

def numbers_product(start, end, step):
    numbers = []
    while start <= end:
        numbers.append(start)
        start += step
    
    multiples_of_3 = [num for num in numbers if num % 3 == 0]
    
    product = 1
    for num in multiples_of_3:
        product *= num
    
    return product


result = numbers_product(1, 20, 2)
print(result) 

#2
def perform_operations(base_number):
    user_number = float(input("Enter a number: "))
    print(f"Base number: {base_number}")
    print(f"User number: {user_number}")
    
    print(f"Addition: {base_number + user_number}")
    print(f"Subtraction: {base_number - user_number}")
    print(f"Multiplication: {base_number * user_number}")
    print(f"Division: {base_number / user_number if user_number != 0 else 'undefined'}")

#3
def hashtag_generator(sentence):
    words = sentence.split()
    hashtag = '#' + ''.join(word.capitalize() for word in words)
    return hashtag

print(hashtag_generator("abc def ghi"))  

#4
def num_divisors(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    return divisors

print(num_divisors(20))  

#5
def manual_split(word, start, end, step):
    result = ''
    i = start
    while i < end and i < len(word):
        result += word[i]
        i += step
    return result

print(manual_split("Hello World!", 2, 6, 2))  