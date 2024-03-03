#number = int(input("Enter a number: "))

#if number % 2 == 0 and number % 4 == 0:
    #print(f"{number} is exactly divisible by 2 and 4.")
#else:
    #print(f"{number} is not exactly divisible by 2 and 4.")

# Greater than
5 > 3

# Less than
7 < 10

# Greater than or equal to
20 >= 18

# Less than or equal to
15 <= 15

# Equal to
"apple" == "apple"

# Not equal to
10 != 5

# Numeric comparison
3.14 < 3.1416

# String comparison
"hello" > "world"

# Boolean comparison
True == False

# Complex comparison
(2 + 3j) != (3 + 2j)

# Both conditions are true
x = 5
y = 10
if x > 0 and y > 5:
    print("Both conditions are true.")

# One condition is false
a = 15
b = 3
if a < 10 and b == 3:
    print("Both conditions are true.")
else:
    print("At least one condition is false.")

# Both conditions involving strings are true
word1 = "hello"
word2 = "world"
if len(word1) > 3 and len(word2) <= 5:
    print("Both conditions are true.")

# One condition involving a boolean is false
flag1 = True
flag2 = False
if flag1 and not flag2:
    print("Both conditions are true.")
else:
    print("At least one condition is false.")

# Both conditions involving numbers are true
num1 = 8
num2 = 12
if num1 * 2 == num2 and num2 % 4 == 0:
    print("Both conditions are true.")