# ducks = ["Huey", "Dewey", "Louie"]
# 
# new_duck = ducks.append(input('Add a duck: '))
# 
# print(f"Updated list of ducks: {ducks}")

def add(prompt, strings):
    strings.append(input(prompt))
    return strings

# Test of the function add with the list ducks.

ducks = ["Huey", "Dewey", "Louie"]

print(f"         Ducks: {ducks}")
print()

ducks_alias = add("    Add a duck: ", ducks)

print(f"         Ducks: {ducks}")
print(f"Alias of Ducks: {ducks_alias}")
print()

# Test of the function add with the list composers.

composers = ["Mozart", "Bach"]
print(f"     Composers: {composers}")
print()

add("Add a composer: ", composers)

print(f"     Composers: {composers}")
print()