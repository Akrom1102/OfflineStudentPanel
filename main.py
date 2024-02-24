import register
import login

def main():
    enter = input("""
    ______________________________________
    
        1. Login
        2. Register

    ______________________________________
            >>> """)

    if enter == "1":
        return login.login_check()

    elif enter == "2":
        return register.register()

    else:
        print("Error!")
        print("_________________________________\n")
        return main()

if __name__ == "__main__":
    main()