from main import main
import classes
import re
import json
import random

def user_info(username, password):
    print(classes.User.get_info(username, password))
    back = input("0. Back\n\t>>> ")
    if back == "0":
        return profile(username, password)
    else:
        print("Xato !")
        print("⭕⭕⭕⭕⭕⭕⭕⭕\n")
        return user_info(username, password)

def change_bill(username, password):
    print("____________________________________________________________")
    new_bill = float(input("""
        Nech pul solmoqchisiz (0 sonidan kattaroq son kiriting !!!)? 
    >>> """))

    while new_bill <= 0:
        print("""
            >>>Siz 0 sonini yoki 0dan kichik son kiritdingiz. Iltimos 0dan kattaroq son kiriting<<<
        """)
        new_bill = float(input("""
            Nech pul solmoqchisiz (0 sonidan kattaroq son kiriting !!!)? 
        >>> """))
    current_bill = classes.User.change_bill(username, password)
    new_money = current_bill + new_bill
    print(classes.User.change("billing", username, password, new_money))
    return user_balance(username, password)

def change_first_name(username, password):
    print("Foydalanuvchining Ismini o'zgartirish")
    new_first_name = input("Yangi Ism: ")
    print(classes.User.change("first_name", username, password, new_first_name))
    return user_change_info(username, password)

def change_last_name(username, password):
    print("Foydalanuvchining Familyasi o'zgartirish")
    new_last_name = input("Yangi Familiya: ")
    print(classes.User.change("last_name", username, password, new_last_name))
    return user_change_info(username, password)

def change_username(username, password):
    print("Foydalanuvchining username o'zgartirish")
    new_username = input("Yangi nik: ")
    with open("Jsonfiles/users.json", 'r') as f:
        users = json.load(f)
        for i in users['users']:
            while i["username"] == new_username:
                print(f""" >>>>>>>>>> Bunday username DATAda mavjud! Iltimos boshqa username kiriting <<<<<<<<<<""")
                new_username = input("Username: ")

    print(classes.User.change("username", username, password, new_username))
    return user_change_info(new_username, password)

def change_password(username, password):
    print("Foydalanuvchining Password o'zgartirish")
    new_password = input("Yangi parol: ")
    print(classes.User.change("password", username, password, new_password))
    return user_change_info(username, new_password)

def change_gmail(username, password):
    print("Foydalanuvchining gmail o'zgartirish")
    new_gmail = input("Yangi email: ")

    def check_gmail(new_gmail):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

        if re.match(pattern, new_gmail):
            return True
        else:
            return False

    while check_gmail(new_gmail) == False:
        print("Noto'g'ri email formati. Iltimos, qaytadan kiriting.")
        new_gmail = input("Yangi email(example@example.com) bolishi shart: ")


    print(classes.User.change("gmail", username, password, new_gmail))
    return user_change_info(username, password)

def change_full_change(username_user, password_user):
    print("Foydalanuvchining To'liq ma'lumotlarini o'zgartirish")
    first_name = input("Ism: ")
    last_name = input("Familiya: ")
    username = input("Username: ")
    with open("Jsonfiles/users.json", 'r') as f:
        users = json.load(f)
        for i in users['users']:
            while i["username"] == username:
                print(f""" >>>>>>>>>> Bunday username DATAda mavjud! Iltimos boshqa username kiriting <<<<<<<<<<""")
                username = input("Username: ")

    password = input("Password: ")
    password_1 = input("Passwordni qayta kiriting: ")
    while password != password_1:
        print("Passwordlar farq qilishi mumkun emas")
        password_1 = input("Password: ")
    gmail = input("Gmail: ")
    def check_gmail(gmail):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

        if re.match(pattern, gmail):
            return True
        else:
            return False

    while check_gmail(gmail) == False:
        print("Noto'g'ri email formati. Iltimos, qaytadan kiriting.")
        gmail = input("Yangi email(example@example.com) bolishi shart: ")


    new_data = {
        "first_name": first_name,
        "last_name": last_name,
        "username": username,
        "password": password,
        "gmail": gmail,
    }
    print(classes.User.change("full_name", username_user, password_user, new_data))
    return user_change_info(username, password)



def user_change_info(username, password):
    about = input("""
        Qaysi ma'lumotlaringizni o'zgartirmoqchisiz:
            1. Ism
            2. Familiya
            3. Username
            4. Password
            5. Gmail
            6. Hammasi
            0 Back
                >>> """)

    if about == "1":
        return change_first_name(username, password)

    elif about == "2":
        return change_last_name(username, password)

    elif about == "3":
        return change_username(username, password)

    elif about == "4":
        return change_password(username, password)

    elif about == "5":
        return change_gmail(username, password)

    elif about == "6":
        return change_full_change(username, password)

    elif about == "0":
        return profile(username, password)

    else:
        print("Error!")
        return user_change_info(username, password)


def user_balance(username, password):
    service = input("""
        Billing:
            1. Balance
            2. Fill balance
            0. Back
    >>>> """)

    if service == "1":
        print(f"""
        _______________________________________________________________
        
            Balance 💲 : {classes.User.billing(username, password)}
            
        _______________________________________________________________
        """)
        return user_balance(username, password)

    elif service == "2":
        print(f"""
        >>>>>>>>>>Sizning balansingiz {classes.User.billing(username, password)}<<<<<<<<<<
        """)
        return change_bill(username, password)

    elif service == "0":
        return profile(username, password)

    else:
        print("""
        ________________________________________________________________
                    Error! Tepadagi sonlardan birini tanlang
        ________________________________________________________________
        """)
        return user_balance(username, password)


def profile(username, password):
    service = input("""
        Profile:
            1. Info about user
            2. Change Info about user
            3. Balance of user
            0. Back
                >>> """)

    if service == "1":
        return user_info(username, password)

    elif service == "2":
        return user_change_info(username, password)

    elif service == "3":
        return user_balance(username, password)

    elif service == "0":
        return user(username, password)

    else:
        print("Error!")
        return profile(username, password)


def user(username, password):
    print("This is user page")

    header = input("""
        1. Profile
        2. Courses
        3. Speciality
        0. Log Out
            >>> """)

    if header == "2":
        data = classes.Course.get_all_course()
        for i in data:
            print(f"""
                Name: {i["name"]}
                Gradution: {i["gradution"]}
                Description: {i["description"]}
                Buying users: {i["buying_users"]}
                Price: {i["price"]}
                Mentor: {i["mentor"]}
                Hours: {i["hours"]}
                Reyting: {i["reyting"]}
                Lenguege: {i["lenguege"]}
            """)
            print("_______________________________________________________________\n")

        buy_course = input(""" 
        >>>>>>>>>> Qaysidir kursni sotib olasizmi? <<<<<<<<<<
            1. Ha
            2. Yo'q
        >>> """)

        if buy_course == "1":
            data = classes.Course.get_all_course()
            print("Qaysi kursni sotib olishingizni tanlang !!!")
            for i in data:
                print("     👇👇👇👇👇👇👇👇👇")
                print(f"    Kurs nomi {i["name"]} ----- Narxi {i["price"]}")
                print("     👆👆👆👆👆👆👆👆👆")
                print("______________________________________________________")
            print("Tanlagan kursingizni nomini kiriting 👇👇👇")
            buy_course = input(">>>")

            with open('Jsonfiles/courses.json', 'r') as f:
                data = json.load(f)
                if buy_course in data:
                    print(f"""
                    >>>>>>>>>> Siz {buy_course} kursini tanladingiz <<<<<<<<<<
                    >>>>>>>>>> Siz {buy_course} kursini sotib oldingiz <<<<<<<<<<
                    """)
                else:
                    print(""">>>>> Bunday kurs mavjud emas!!! Iltimos tepada bor kurslardan birini tanlang <<<<<""")
                    print("Tanlagan kursingizni nomini kiriting 👇👇👇")
                    buy_course = input(">>>")

        return user(username, password)


    elif header == "3":
        data = classes.Speciality.get_all_speciality()
        for i in data:
            print(f"""
                name: {i["name"]}
                description: {i["description"]}
                gradution: {i["gradution"]}
                create_date: {i["create_date"]}
            """)
            print("__________________________________________\n")
        return user(username, password)

    elif header == "1":
        return profile(username, password)

    elif header == "0":
        return main()

    else:
        print("Error!\n Bunday servis yo'q")
        return user(username, password)