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

options1 = {"a":"Add item", "l":"List items", "q":"Log out"}
opt1 = menu("Select an action", "Action: ", options1)
print(f"You selected action {opt1}) {options1[opt1]}")
print()

options2 = {"r":"Try again", "q":"Quit"}
opt2 = menu("What do you want to do?", "My choice: ", options2)
print(f"You selected option {opt2}) {options2[opt2]}")