from faker import Faker

class FakeDataGenerator:
    def __init__(self):
        self.fake = Faker()
        self.fake_username = self.fake.first_name()
        self.fake_email = self.fake.email()
        self.fake_password = self.fake.password(length=12)
