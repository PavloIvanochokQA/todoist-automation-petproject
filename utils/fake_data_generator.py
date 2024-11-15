from faker import Faker


class FakeDataGenerator:
    def __init__(self):
        self.fake = Faker()
        self.username = self.fake.first_name()
        self.email = self.fake.email()
        self.password = self.fake.password(length=12)
