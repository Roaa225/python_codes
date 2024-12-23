
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print("My name is :",self.name)
        print("My age is :",self.age)

class Engineer(Person):
    def __init__(self, name, age, specialty):
        super().__init__(name, age)  
        self.specialty = specialty
    
    def work(self):
        print("I am an engineer specializing in:", self.specialty)


class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)  
        self.specialization = specialization
    
    def work(self):
        print("I am a doctor specializing in :", self.specialization)


engineer = Engineer("Ahmed", 30, "Civil Engineering")
doctor = Doctor("Fatima", 40, "Surgery")
engineer.display_info()  
engineer.work()  
doctor.display_info()  
doctor.work()  
