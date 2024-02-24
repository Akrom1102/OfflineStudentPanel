import json
from datetime import datetime

class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return f"{self.username} {self.password}"

class User(Login):
    def __init__(self, username: str, password: str, first_name: str, last_name: str, gmail: str, status: bool, billing):
        Login.__init__(self, username, password)
        self.first_name = first_name
        self.last_name = last_name
        self.gmail = gmail
        self.status = status
        self.billing = billing
        self.create_date = datetime.now().date()

    @staticmethod
    def change_bill(username, password):
        with open("Jsonfiles/users.json", 'r') as file:
            data = json.load(file)
            users = data["users"]
            for i in users:
                if i['username'] == username and i["password"] == password:
                    return i['billing']





    @staticmethod
    def billing(username, password):
        with open("Jsonfiles/users.json", "r") as f:
            data = json.load(f)

            for i in data["users"]:
                if i["username"] == username and i["password"] == password:
                    user_billing = i["billing"]
            return user_billing

    @staticmethod
    def get_info(username, password):
        with open("Jsonfiles/users.json", "r") as file:
            data = json.load(file)

            for i in data["users"]:
                if i["username"] == username and i["password"] == password:
                    user = f"""
                        First name: {i["first_name"]}
                        Last name: {i["last_name"]}
                        Username: {i["username"]}
                        Password: {i["password"]}
                        Gmail: {i["gmail"]}
                        Billing: {i["billing"]}
                    """
            return user

    @staticmethod
    def see_users():
        with open("Jsonfiles/users.json", "r") as file:
            data = json.load(file)

            for i in data['users']:
                print(f"""
                    Username: {i["username"]}
                    First name: {i["first_name"]}
                    Last name: {i["last_name"]}
                    Gmail: {i["gmail"]}
                    Billing: {i["billing"]}
                    __________________________________
                    Siz Foydalanuvchini Parolini ko'ra olmaysiz !
                    __________________________________
                """)

    @staticmethod
    def change(argument, username, password, new_data):
        if argument != "full_name":
            with open("Jsonfiles/users.json", "r") as file:
                data = json.load(file)
                users = data["users"]
                for i in users:
                    if i["username"] == username and i["password"] == password:
                        user = i
                users.remove(user)
                user[argument] = new_data
                users.append(user)
                data["users"] = users

            with open("Jsonfiles/users.json", "w") as f:
                json.dump(data, f, indent=6)
            return "Sucsessfull"
        else:
            with open("Jsonfiles/users.json", "r") as file:
                data = json.load(file)
                users = data["users"]
                for i in users:
                    if i["username"] == username and i["password"] == password:
                        user = i
                users.remove(user)
                keys = new_data.keys()
                for i in keys:
                    user[i] = new_data[i]
                users.append(user)
                data["users"] = users

            with open("Jsonfiles/users.json", "w") as f:
                json.dump(data, f, indent=6)
            return "Sucsessfully"

    def __str__(self):
        return f"{self.username} {self.password} {self.first_name}  {self.last_name} {self.gmail} {self.status} {self.create_date}"

class Register(User):
    def __init__(self, username, password, first_name, last_name, gmail, status, billing):
        User.__init__(self, username, password, first_name, last_name, gmail, status, billing)
        self.create_date = f"{datetime.now().date()}"

    def save_data_user(self):
        with open("Jsonfiles/users.json", "r") as file:
            data = json.load(file)
            new_user = {
                "username": self.username,
                "password": self.password,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "gmail": self.gmail,
                "status": self.status,
                "billing": self.billing,
                "create_date": self.create_date
            }
            users = data["users"]
            users.append(new_user)
            data["users"] = users

        with open("Jsonfiles/users.json", "w") as f:
            json.dump(data, f, indent=6)


class Student(User):
    def __init__(self, username, password, first_name, last_name, gmail, status: 0, courses: list):
        User.__init__(self, username, password, first_name, last_name, gmail, status, billing=0)
        self.courses = courses

class Speciality:
    def __init__(self, name: str, description: str, gradution):
        self.name = name
        self.description = description
        self.gradution = gradution
        self.create_date = datetime.now()

    @staticmethod
    def get_all_speciality():
        with open("Jsonfiles/speciality.json", "r") as file:
            data = json.load(file)
            return data["speciality"]

class Course:
    def __init__(self, name: str, gradution: int, description: str, buying_users: int, price: float, mentor: str, hours: float, reyting: float, active_users: int, lenguege: str):
        self.name = name
        self.gradution = gradution
        self.description = description
        self.buying_users = buying_users
        self.price = price
        self.mentor = mentor
        self.hours = hours
        self.reyting = reyting
        self.active_users = active_users
        self.lenguege = lenguege
        self.create_date = f"{datetime.now().date()}"

    def save_new_course(self):
        with open("Jsonfiles/courses.json", "r") as file:
            data = json.load(file)
            new_course = {
                "name": self.name,
                "gradution": self.gradution,
                "description": self.description,
                "buying_users": self.buying_users,
                "price": self.price,
                "mentor": self.mentor,
                "hours": self.hours,
                "reyting": self.reyting,
                "active_users": self.active_users,
                "lenguege": self.lenguege,
                "create_date": f"{datetime.now().date()}"
            }
            courses = data["courses"]
            courses.append(new_course)
            data["courses"] = courses

        with open("Jsonfiles/courses.json", "w") as f:
            json.dump(data, f, indent=6)

    @staticmethod
    def get_all_course():
        with open("Jsonfiles/courses.json", "r") as file:
            data = json.load(file)
            return data["courses"]