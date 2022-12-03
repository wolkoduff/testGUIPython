from Person import Person

def showInformation():
    value = input("Введите текст: ")
    print(value)

sasha = Person("Sasha", 10, "Male")
sasha.showInfo()
print("----------------")

tanya = Person("Tanya", 20, "Female")
tanya.showInfo()
print("----------")

default = Person("Default")
default.showInfo()
print("-------\n\n")

showInformation()

#f = open("claim.txt", 'r', encoding="utf8")
#print(f.read())
