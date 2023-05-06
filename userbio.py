class User:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def info(self):
        return (self.name, self.age)

    def cities(self):
        return self.city

#create an instance
user = User("John", 35, "Maryland")

print("UserData:", user.info())
print("City:", user.cities())

