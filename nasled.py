class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat_spaghetti(self):
        return f'я могу есть спагетти'

class Robot:
    def __init__(self, model, energy):
        self.model = model
        self.energy = energy
    def drink_oil(self):
        return f'Я могу потреблять машинное масло'

class Cuborg(Human, Robot):
    def  __init__(self, name, company, model):
        self.name = name
        self.company = company
        self.model = model

result = Cuborg('adi', 'it-academy', 'f22')
print(result.eat_spaghetti())
print(result.drink_oil())
print(result.company)