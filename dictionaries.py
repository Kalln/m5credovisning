users = {"nisse":"apa", "bosse":"ko", "stina":"t-rex"}

# skriver ut varje nyckel i users, i detta fall är nyckel användarnamnet
print('Användare')
for k in users:
    print(f"    {k}")
    
# Skriver ut användare och lösenord som vi har i dictionary "users"
print('\nAnvändare och lösenord: ')
for k, v in users.items():
    print(f"{k}) {v}")

# Ny dictionary med listor som värde som innehåller data
# nyckeln i detta fall är namnet på personen
data = {"nisse":["luva", "vante"],
        "bosse":["spik", "skruv","hammare"],
        "stina":["tidsmaskin"]}


# Skriver ut användare och dess data
print('\nAnvändare och deras data')
for k, v in data.items():
    print(f"{k}) {v}")
    
    
# Kontrollerar om angiven användare finns i systemet.
# Om det finns så skriver vi ut datan som vi har på den användaren
# genom att skriva ut värdet för den nyckeln.
# Om den inte finns så skriver vi ut det.
user_to_check = input('\nSlå upp användare: ')
if user_to_check in data:
    print(f"Data lagrad för {user_to_check}: {data[user_to_check]}")
else: print(f"Användaren {user_to_check} finns inte")
    