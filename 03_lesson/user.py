class User:
    def __init__(self, first_name, last_name):
        self.f_name = first_name
        self.l_name = last_name

    def get_first_name(self):
        print(self.f_name)

    def get_last_name(self):
        print(self.l_name)

    def get_product_info(self):
        print(self.f_name, self.l_name)