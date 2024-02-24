import json
import admin_page
import user_page
import register


def login_check():
    print("Login Page")
    username = input("Username: ")
    password = input("Password: ")
    with open("Jsonfiles/users.json", 'r') as file:
        data = json.load(file)
        for i in data["users"]:
            if i["username"] == username and i["password"] == password:
                if i["status"] == 1:
                    return admin_page.admin_page(username, password)
                else:
                    return user_page.user(username, password)
        print("""
            Error!
            Bunday foydalanuvchi mavjud emas yoki ma'lumotlar xato kiritildi!
        """)
        print("___________________________________________________________\n")

        no_login = input(""" 👨‍🎓 Tizimdan ro'yxatdan o'tishni xoxlaysizmi !👇
            1. Ha 
            2. Yo'q ❌
        >>> """)
        if no_login == '1':
            return register.register()

        elif no_login == '2':
            return login_check()

        else:
            print("Error ⭕⭕")
            print("""Iltimos tepada ko'rsatilgan sonlardan birini yanlang !
            ______________________________________________________________""")


        return login_check()