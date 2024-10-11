username = input()
password = input()

while True:
    entered_password = input()

    if entered_password == password:
        print(f"Welcome {username}!")
        break
    else:
        print()
