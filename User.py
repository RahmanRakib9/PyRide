# user.py
class User:
    def __init__(self, name, email, nationalId):
        self.name = name
        self.email = email
        self.nationalId = nationalId
        self.wallet = 0

    def displayProfile(self):
        print(f'UserName: {self.name}, UserEmail: {self.email}')
