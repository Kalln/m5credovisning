options1 = {"a":"Add item",
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

user1 = "nisse"
user2 = "bosse"

items1 = ["luva", "vante"]
items2 = ["hammare", "skruv", "spik"]

user_actions(user1, items1)
print(f"Goodbye {user1}, your items: {items1}")
print()

user_actions(user2, items2)
print(f"Goodbye {user2}, your items: {items2}")
print()