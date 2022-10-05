options = {"a":"Add item", "l":"List items", "q":"Log out"}

print('Select an action')
while True:
    user_input = input('Option: ')
    match user_input:
        case 'a':
            print(f"You selected option a) {options[a]}")
            break