import json
import classes
import main
import re

def change_first_name(username, password):
    print("Adminnning Ismini o'zgartirish")
    new_first_name = input("Yangi Ism: ")
    print(classes.User.change("first_name", username, password, new_first_name))
    return admin_change_info(username, password)

def change_last_name(username, password):
    print("Adminnning Familyasini o'zgartirish")
    new_last_name = input("Yangi Familiya: ")
    print(classes.User.change("last_name", username, password, new_last_name))
    return admin_change_info(username, password)

def change_username(username, password):
    print("Adminnning usernameini o'zgartirish")
    new_username = input("Yangi nik: ")
    print(classes.User.change("username", username, password, new_username))
    return admin_change_info(new_username, password)

def change_password(username, password):
    print("Adminnning Passwordini o'zgartirish")
    new_password = input("Yangi parol: ")
    print(classes.User.change("password", username, password, new_password))
    return admin_change_info(username, new_password)

def change_gmail(username, password):
    print("Adminnning gmailini o'zgartirish")
    new_gmail = input("Yangi email(example@example.com) bolishi shart: ")

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
    return admin_change_info(username, password)

def change_full_change(username_user, password_user):
    print("Adminnning To'liq ma'lumotlarini o'zgartirish")
    first_name = input("Ism: ")
    last_name = input("Familiya: ")
    username = input("Username: ")
    password = input("Password: ")
    password_1 = input("Passwordni qayta kiriting: ")
    while password != password_1:
        print("Passwordlar farq qilishi mumkun emas")
        password_1 = input("Password: ")
    gmail = input("Gmail (example@gmail.com) shunday bolishi shart: ")

    def check_gmail(gmail):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

        if re.match(pattern, gmail):
            return True
        else:
            return False

    while check_gmail(gmail) == False:
        print("Noto'g'ri email formati. Iltimos, qaytadan kiriting.")
        gmail = input("Email (@example.com bo'lishi shart): ")


    new_data = {
        "first_name": first_name,
        "last_name": last_name,
        "username": username,
        "password": password,
        "gmail": gmail,
    }
    print(classes.User.change("full_name", username_user, password_user, new_data))
    return admin_change_info(username, password)


def admin_info(username,password):
    print(classes.User.get_info(username,password))
    back = input("0. Back \n \t >>>")
    if back == "0":
        return admin_profile(username,password)

    else:
        print("___________________________________________")
        print("Xato !")
        print("___________________________________________")

def admin_change_info(username, password):
    about = input("""
    ______________________________________________________
        Qaysi ma'lumotlaringizni o'zgartirmoqchisiz:
            1. Ism
            2. Familiya
            3. Username
            4. Password
            5. Gmail
            6. Hammasi
            0 Back
    ______________________________________________________
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
        return admin_profile(username, password)

    else:
        print("Error!")
        return admin_change_info(username, password)

def admin_profile(username, password):
    service = input("""
    ______________________________________________________
        Profile:
            1. Info about Admin
            2. Change Info about user
            0. Back
    ______________________________________________________
                >>> """)

    if service == "1":
        return admin_info(username, password)

    elif service == "2":
        return admin_change_info(username, password)

    elif service == "0":
        return admin_page(username, password)

    else:
        print("Error!")
        return admin_profile(username, password)

def admin_page(username, password):
    print(">>>>>>>>>>>This is ADMIN page<<<<<<<<<<<<<")

    header = input("""
    ______________________________________________________
    
        1. Profile
        2. Courses
        3. See All Users
        0. Log Out
        
    ______________________________________________________
            >>> """)

    if header == "2":
        data = classes.Course.get_all_course()
        for i in data:
            print(f"""
            ______________________________________________________
            
                Name: {i["name"]}
                Gradution: {i["gradution"]}
                Description: {i["description"]}
                Buying users: {i["buying_users"]}
                Price: {i["price"]}
                Mentor: {i["mentor"]}
                Hours: {i["hours"]}
                Reyting: {i["reyting"]}
                Lenguege: {i["lenguege"]}
                
            ______________________________________________________
            """)
            print("_________________________________________\n")

        admin_add_course = input("""
            >>>>>>> Yangi Kurs qo'shmoqchimisiz ? <<<<<<<
                1. Ha 
                2. Yo'q 
        >>> """)

        if admin_add_course == "1":
            print("Add Course page\n")
            print("Yangi KURS qo'shish uchun quyidagilarni to'ldiring 👇👇:")
            name = input("Name of course: ")
            gradution = int(input("Graduatoin (kursning davomiyligi): "))
            description = input("Description: ")
            price = float(input("Price: "))
            mentor = input("Mentor: ")
            hours = int(input("Hours: "))
            languege = input("Language: ")

            add_course = classes.Course(name, gradution, description, 0, price, mentor, hours, 1, 1, languege)
            print("_____________________________________________________________________________________")
            print("Yangi Kurs Muvaffaqqiyatli qo'shildi")
            print("_____________________________________________________________________________________")
            add_course.save_new_course()

            return admin_page(username, password)

        elif admin_add_course == "2":
            return admin_page(username, password)

        else:
            print("Xatoo! Tepada korsatilgan sonlardan birini tanlang !")

            return admin_add_course


        # return admin_page(username, password)


    elif header == "3":
        data = classes.User.see_users()
        print(data)
        print("__________________________________________\n")
        return admin_page(username, password)

    elif header == "1":
        return admin_profile(username, password)

    elif header == "0":
        return main.main()

    else:
        print("Error!\n Bunday servis yo'q")
        return admin_page(username, password)