def view(description, strings):
    print(description)
    for i in range(len(strings)):
        print(f"{i+1}) {strings[i]}")
        
names   = ["nisse", "stina", "bosse", "mimmi"]
animals = ["giraff", "myrslok", "tapir"]

view("Lista med namn", names)
print()
view("Lista med djur", animals)
