class UserModel:
    def __init__(self, first_name: str = None, last_name: str = None, email: str = None, password: str = None):
        self.id = None
        self.first_name = first_name
        self.last_name = last_name
        self.email = f'{self.first_name.lower()}_{self.last_name.lower()}@gmail.com' if not email else email
        self.password = password
