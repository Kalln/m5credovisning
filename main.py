options_login = {"l":"log in",
                "q":"quit"}

options_loggedin = {"a":"Add item",
                    "l":"List items",
                    "q":"Log out"}

def menu(title, prompt, options):
    print(title)
    for key, action in options.items():
        print(f"    {key}) {action}")

    # Starta while-loop som väntar på att den får ett kommando 
    # som finns i options dictionarien. Vi gör som i dictionaries.py
    while True: 
        user_option = input(prompt)
        if user_option in options: # Kontrollera om det finns en nyckel som användaren har matat in
            return user_option

def add(prompt, strings):
    strings.append(input(prompt))
    return strings

def view(description, strings):
    print(description)
    for i in range(len(strings)):
        print(f"{i+1}) {strings[i]}")


def user_actions(user, items):
    print(f"Welcome {user}")
    view('These are your items', items)
    while True: 
        user_option = menu('Select an action ', 'Option: ', options1)

        if ('a' == user_option):
            add("Add item: ", items)
        elif ('l' == user_option):
            view("These are your items", items)
        if ('q' == user_option):
            break

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

def main():
    users = {"nisse":"apa",
            "stina":"t-rex",
            "bosse":"ko"}

    data  = {"nisse":["luva", "vante"],
            "stina":[],
            "bosse":["gräs", "mjölk"]}        

    print('Welcome to Lagra (TM)')
    while True: 
        user_input = menu("Welcomet to Lagra (TM)", "Option: ", options_login)
        if (user_input == 'l'):
            login_user = login(users)
            if (login_user != None):
                print("Welcome", login_user)
                



main()