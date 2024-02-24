import classes
from login import login_check
import re
import json
import random

def register():
    print("Register Page\n")
    print("Tizimdan ro'yxatdan o'tish uchun quyidagi ma'lumotlarni kiriting:")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    username = input("Username: ")
    with open("Jsonfiles/users.json", 'r') as f:
        users = json.load(f)
        for i in users['users']:
            while i["username"] == username:
                print(f""" >>>>>>>>>> Bunday username DATAda mavjud! Iltimos boshqa username kiriting <<<<<<<<<<
                Masalan:
                    1. {first_name + str(random.randint(1, 10000))}
                    2. {last_name + str(random.randint(1, 10000))}
                    3. Yoki o'zingiz boshqa xoxlagan usrname kiriting 
                """)
                username = input("Username: ")


    password = input("Password: ")
    password_1 = input("Password: ")
    while password != password_1:
        print("Passwordlar farq qilishi mumkun emas")
        password_1 = input("Password: ")
    gmail = input("Gmail (example@example.com) bo'lishi shart: ")

    def check_gmail(gmail):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

        if re.match(pattern, gmail):
            return True
        else:
            return False

    while check_gmail(gmail) == False:
        print("Noto'g'ri email formati. Iltimos, qaytadan kiriting.")
        gmail = input("Yangi email(example@example.com) bolishi shart: ")

    if password == password_1:
        register = classes.Register(username, password, first_name, last_name, gmail, 0, 0)
        print("_____________________________________________________________________________________")
        print("Successfull")
        print("_____________________________________________________________________________________")
        register.save_data_user()
        return login_check()