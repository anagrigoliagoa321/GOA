#homework
games = ["Pubg mobile", "roblox", "minecraft"]

games = ["sololearn", "w3", "codewars"]
print("Updated Games List:", games)


#2
numbers = []

for _ in range(5):
    num = int(input("Enter a number: "))
    numbers.append

even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers:", even_numbers)


#3
numbers = [int(input("Enter number {}: ".format(i+1))) for i in range(5)]

total = 0
for num in numbers:
    total += num

print("Sum of the list:", total)

#4
numbers = [int(input("Enter number {}: ".format(i+1))) for i in range(10)]

# Find the largest number
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print("Largest number:", largest)


#5
numbers = list(range(30, 50))

odd_count = sum(1 for num in numbers if num % 2 != 0)
print("Count of odd numbers:", odd_count)

#6
multiples_of_4 = [num for num in range(10, 50) if num % 4 == 0]

print("Multiples of 4 in reverse:", multiples_of_4[::-1])

#7

numbers = list(range(50, 101))

for index, num in enumerate(numbers):
    if num % 2 == 0:
        print(f"[num] - [index]")