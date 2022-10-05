def add(prompt, strings):
    strings.append(input(prompt))
    return strings

def view(description, strings):
    print(description)
    for i in range(len(strings)):
        print(f"{i+1}) {strings[i]}")
        
strings = []
n = 2

print(f"n = {n}")

for _ in range(n):
    add('Lägg till en sträng: ', strings)
    
view(f'\nDu har matat in följande {n} strängar\n', strings)