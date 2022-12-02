class Customers:
    def __init__(self, first_name, second_name, city):
        self.first_name = first_name
        self.second_name = second_name
        self.city = city

    def get_guest(self):
        return f'{self.first_name} {self.second_name}, г. {self.city}'

costomer_1 = Customers('Иван', 'Петров', 'Москва')
costomer_2 = Customers('Владимир', 'Зайцев', 'Кострома')
costomer_3 = Customers('Олеся', 'Янина', 'Новосибирск')

guest_list=[costomer_1, costomer_2, costomer_3]

for guest in guest_list:
    print(guest.get_guest())