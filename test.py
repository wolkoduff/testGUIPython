from Person import Person

sasha = Person("Sasha", 10, "Male")
sasha.showInfo()
print("----------------")

tanya = Person("Tanya", 20, "Female")
tanya.showInfo()
print("----------")

default = Person("Default")
default.showInfo()
print("-------")

f = open("claim.txt", 'r', encoding="utf8")
print(f.read())
