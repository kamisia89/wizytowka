from faker import Faker

f = Faker("en_GB")
f = Faker()


class BaseContact:
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.name = 0
        self.label_lenght = len(first_name) + len(last_name)

    # def get_contact(self, first_name, last_name, phone_number, email):
    # return self.first_name, self.last_name, self.phone_number, self.email
    def __str__(self):
        return f"{self.first_name}{self.last_name}{self.phone_number}{self.email}"

    def __repr__(self):
        return f"{self.first_name}{self.last_name}{self.phone_number}{self.email}"

    def contact(self):
        return (
            f"Kontaktuje się z: {self.first_name} {self.last_name} {self.phone_number} "
        )


# contact = BaseContact()
person_1 = BaseContact(
    first_name="Robert ",
    last_name="Kelly ",
    phone_number=9726397253,
    email=" blairlarry@example.com ",
)
person_2 = BaseContact(
    first_name="Jaime ",
    last_name="Reese ",
    phone_number=9726397253,
    email=" amurphy@example.net",
)
person_3 = BaseContact(
    first_name="Debra ",
    last_name="Mason ",
    phone_number=7435350260,
    email=" ulynn@example.net",
)
person_4 = BaseContact(
    first_name="Jon ",
    last_name="Padilla ",
    phone_number=7654563239,
    email=" nancywolfe@example.net ",
)
person_5 = BaseContact(
    first_name="Sarah",
    last_name="Bell",
    phone_number=7769866745,
    email="crystal74@example.com",
)

print(person_1, person_2, person_3, person_4, person_5)
persons = (person_1, person_2, person_3, person_4, person_5)

by_first_name = sorted(persons, key=lambda BaseContact: BaseContact.first_name)
lambda BaseContact: BaseContact.first_name
print("sortowanie po imieniu:")
print(by_first_name)
by_last_name = sorted(persons, key=lambda BaseContact: BaseContact.last_name)
lambda BaseContact: BaseContact.last_name
print("sortowanie po nazwisku:")
print(by_last_name)
by_email = sorted(persons, key=lambda BaseContact: BaseContact.email)
lambda BaseContact: BaseContact.email
print("sortowanie po e-mailu:")
print(by_email)


@property
def label_lenght(self):
    return sum([len(self.first_name), len(self.last_name)])


class BusinessContact(BaseContact):
    def __init__(self, position, company, company_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        self.phone = company_phone

    def contact(self):
        return f"Wybieram numer: {self.phone_number} i dzwonię do: {self.first_name} {self.last_name}"


def create_contacts(self):
    f.first_name()
    f.last_name()
    f.phone_number()
    f.email()
    f.job()
    f.company()
    f.phone_number()


for _ in range(5):
    print(
        f.first_name(),
        f.last_name(),
        f.phone_number(),
        f.email(),
        f.job(),
        f.company(),
        f.phone_number(),
    )


print(person_1, f"ilość liter: ", person_1.label_lenght)
print(person_2, f"ilość liter: ", person_2.label_lenght)
print(person_3, f"ilość liter: ", person_3.label_lenght)
print(person_4, f"ilość liter: ", person_4.label_lenght)
print(person_5, f"ilość liter: ", person_5.label_lenght)
