class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
        
    def bark(self):
        print("woof!")

class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.contact_number = contact_number
    



owner1 = Owner('Jeremy', '112 High Street', '01234567890')
dog1 = Dog("sally", "pug", owner1)

print(dog1.owner.name)

owner2 = Owner('Susan', '112 Low Street', '01234567899')
dog2 = Dog("luke", "shepherd", owner2)
print(dog2.owner.name)
