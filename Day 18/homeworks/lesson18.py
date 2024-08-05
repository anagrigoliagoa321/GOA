#შექმენით ფუნქცია, რომელსაც გადაეცემა 1-იდან 20-ის ჩათვლით რიცხვების სია. თქვენ უნდა დააბრუნოთ გაფილტრული სია, სადაც უკვე მარტო 4-ის ჯერადები იქნება.
def filter_multiples_of_4(numbers):
    return[num for num in numbers if num % 4 == 0]


#შექმენით ფუნქცია, რომელსაც გადასცემთ მომხმარებლისგან მიღებულ სახელსა და გვარს. შემდეგ ისინი დაამატეთ სიაში და დააბრუნეთ სია.
def add_name_to_list():
    first_name = input("Enter your first name: ")
    Last_name = input("Enter your Last name: ")
    return(first_name,Last_name)


#მომხმარებელს შეეკითხეთ საწყისი და საბოლოო რიცხვები. ეს რიცხვები გადაეცით ფუნქციას, for ციკლით სიაში შეინახეთ მათ შორის არსებული რიცხვები. შემდეგ მოახდინეთ გაფილტვრა, ისევ for ციკლით განიხილეთ თითოეული რიცხვი - თუ რიცხვი ლუწი იქნება, ახალ სიაში დაამატეთ მისი მეორე ხარისხი, ხოლო თუ კენტი იქნება სიაში დაამატეთ მისი კვადრატული ფესვი (0.5 ხარისხი).
def filter_numbers_and_operate(start, end):
    numbers_list = []
    for num in range(start, end + 1):
        numbers_list.append(num)
    result = []
    for num in numbers_list:
        if num % 2 == 0:
            result.append(num ** 2)
        else:
            result.append(num ** 0.5)
    return result


#შექმენით ფუნქცია, რომელსაც გადასცემთ მომხმარებლის გვარს. გვარის თითოეული ასო გადაიტანეთ ახალ სიაში. შემდეგ for ციკლის გამოყენებით იმუშავეთ ამ სიაზე - მარტო ლუწ ინდექსებზე მყოფი ასოები დაამატეთ ახალ სიაში. საბოლოოდ დააბრუნეთ ეს სია.
#Bonus (არაა სავალდებულო): ეს სია გარდაქმენით სთრინგად და ამ სახით დააბრუნეთ.
def extract_even_letters(last_name):
    even_letters = []
    for i in range(len(last_name)):
        if i % 2 == 0:
            even_letters.append(last_name[i])
    return ''.join (even_letters)


#შექმენით ფუნქცია, რომელიც მიიღებს მომხმარებლისგან სიტყვას. შემდეგ თქვენ უნდა მოახდინოთ ამ სიტყვის შებრუნება, მაგ: word - drow. საბოლოდ კი დააბრუნეთ შედეგი.
def reverse_word(word):
    return word[::-1]

#შექმენით ფუნქცია,რომელიც მიიღებს რიცხვების სიას და ტქვენ დაააბრუნებთ მის გაფილტრულ ვერსიას,რომელსაც არ აქვს დუპლიკატები(ერტი და იგივე ელემენტები)
def remove_duplicates(numbers):
    return list(set(numbers))





