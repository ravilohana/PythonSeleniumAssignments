from faker import Faker


faker = Faker()

print(f"{faker.name()}")
print(f"{faker.first_name()}")
print(f"{faker.middle_name()}")
print(f"{faker.last_name()}")
print(f"{faker.password()}")