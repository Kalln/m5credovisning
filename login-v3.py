def login(users):
        while True: 
            user = input('    User: ')
            password = input('Password: ')

            if user in users and password == users[user]:
                return user
                break
            else: 
                userTry = menu('Invalid username or password', 'Option: ', options)
                if userTry == 'q':
                    user = None
                    break
def menu(title, prompt, options):
    print(title)
    for key, action in options.items():
        print(f"    {key}) {action}")

    while True: 
        userTry = input(prompt)
        if userTry == 'r' or userTry == 'q': 
            return userTry


users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}
options = {"r":"Try again", "q": "Quit"}
user = login(users)