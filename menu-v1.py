options = {"a":"Add item", "l":"List items", "q":"Log out"}

# Kopierat över functionen view() från input-list-of-strings.py
# men den hanterar nu dictionaries istället för listor.
def view(description, strings):
    print(description)
    for key, action in options.items():
        print(f"    {key}) {action}")

def menu():
    view('Select an action: ', options)

    # Starta while-loop som väntar på att den får ett kommando 
    # som finns i options dictionarien. Vi gör som i dictionaries.py
    while True: 
        user_option = input('Option: ')
        if user_option in options: # Kontrollera om det finns en nyckel som användaren har matat in
            print(f"You have selected option {user_option}) {options[user_option]}")
            break

menu()