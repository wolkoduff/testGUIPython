class Person:
    def __init__(self, 
                 name,         # Имя
                 age=15,       # Возраст
                 gender="Male" # гендер
                ): 
        self.name = name
        self.age = age
        self.gender = gender

    def showInfo(self):
        print("Name: ", self.name)      # Вывести Name: Имя
        print("Age: ", self.age)        # Вывести Age: Возраст
        print("Gender: ", self.gender)  # Вывести Gender: гендер
