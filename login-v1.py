users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}

def login():
    while True: 
        user = input('    User: ')
        password = input('Password: ')

        if user in users and password == users[user]:
            print('\nWelcome', user)
            break
        else: print("\nInvalid username or password\n")

login()