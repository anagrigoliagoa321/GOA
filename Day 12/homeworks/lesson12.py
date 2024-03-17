#მომხმარებელს შემოატანინეთ სახელი, გვარი, ასაკი და საცხოვრებელი ადგილი. თითოეული მათგანი append-ის გამოყენებით დაამატეთ სიაში. slicing-ის გამოყენებით დაბეჭდეთ 1: სახელი, გვარი, 2: გვარი, ასაკი, 3: სახელი, გვარი, ასაკი 4: გვარი, ასაკი, საცხოვრებელი ადგილი.

# name = input("Please enter your name")
# lastname = input("Please enter your lastname")
# age = input("Please enter your name")
# address = input("Please enter your address")

# info = []
# info.append(name)
# info.append(lastname)
# info.append(age)
# info.append(address)

# print(info)

# print(info[0:2])
# print(info[1:3])
# print(info[0:3])
# print(info[1:])

#მომხმარებელს შემოატანინეთ უარყოფითი რიცხვი. ამ რიცხვიდან 0-მდე არსებული ყველა უარყოფითი რიცხვი დაამატეთ სიაში და საბოლოოდ დაბეჭდეთ სია.

# num = int(input("Please enter our negative num : "))
# my_list = []
# for i in range(num,0) :
#     my_list.append(i)
# print(my_list)

#ცვლადში შეინახეთ თქვენი სახელი და გვარი. Slicing-ის გამოყენებით ჯერ სახელი, შემდეგ კი გვარი დაბეჭდეთ.

# name_lastname = ["Anna", "Grigolia"]
# print(name_lastname[0:1])
# print(name_lastname[1:2])

#სიაში შეინახეთ მინიმუმ 5 საყვარელი ფილმი. გამოიყენეთ Slicing და  დაბეჭდეთ რამდენიმე კომბინაციით. Bonus (არ არის აუცილებელი): იგივე კომბინაციები დაბეჭდეთ უარყოფითი ინდექსების გამოყენებით.

# films = ["The Ultimate Gift , The Boy and The Heron , Oppenheimer , Where The Crawdads Sing , Final Destination"]
# print(films[0:2])
# print(films[-4:-1])
# print(films[3:5])
# print(films[4:5])

#მომხმარებელს შემოატანინეთ აკადემიის სახელი. თუ ის "G"-თი იწყება, დაუპრინტეთ რომ გოა არის საუკეთესო არჩევანი. სხვა შემთხვევაში დაუპრინტეთ, რომ არასწორი გადაწყვეტილება მიიღო.

# academy = input("enter your academy: ")
# if academy.startswith("G"):
#     print("Goa is best academy")
# else:
#     print("you make bed choice")
