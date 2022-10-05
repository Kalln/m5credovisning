def add(prompt, strings):
    strings.append(input(prompt))
    return strings

def view(description, strings):
    print(description)
    for i in range(len(strings)):
        print(f"{i+1}) {strings[i]}")
        
strings = []
