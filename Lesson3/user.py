class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_first_name(self):#выводиит толькоо имя
        print(self.first_name)

    def print_last_name(self):#выводит только фамилию
        print(self.last_name)

    def print_full_name(self): #выводит полне имя
        print(f"{self.first_name} {self.last_name}")