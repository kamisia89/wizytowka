from faker import Faker
from faker.providers import DynamicProvider

travel_professions_provider = DynamicProvider(
    provider_name="travel_profession",
    elements=[
        "hotel manager",
        "cruise ship steward",
        "cabin crew",
        "tourist guide",
        "tour manager",
        "travel agent",
        "sailing instructor",
    ],
)
fake = Faker()
fake.add_provider(travel_professions_provider)


class BaseContact:
    def __init__(self, name, surname, phone_number, email):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.email = email
        self.name = 0


class BusinessContact(BaseContact):
    def __init__(self, occupation, company, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.role = role
        self.company = company
        self.business_phone = business_phone


def __repr__(self):
    return f"{self.business_phone} {self.name} {self.surname}"


def contact(self):
    return f"Wybieram numer {self.business_phone}{self.phone_number} i dzwonię do {self.name}{self.surname}”."


# basic = BaseContact()

# TO PSUJE CALY KOD => card = Card()

# def contact(self):
#   return f"{self.name}{self.surname}


# TEN FKER JEST SUPER WYMYSLIL MI IMIONA ITD. ALE MUSIALAM I TAK WSZYSTKO SKOPIOWAC BO JAK MIALAM WSZYSTKO WYMIENIONE W KUPIE NIE WIEDZILAM JAK TO POGRUPOWACI DUPA
def create_contacts(num_contacts):
    contact_list = []


for i in range(1, num_contacts):
    contact = {}
    contact["name"] = fake.name()
    contact["surname"] = fake.surname()
    contact["phone_number"] = fake.phone()
    contact["email"] = fake.email()
    contact["role"] = fake.random_element(
        elements=(
            "Hotel Manager",
            "Travel Agent",
            "Tour Operator",
            "Tourist Guide",
            "Tour Manager",
            "Sailing Instructor",
        )
    )
    contact["company"] = fake.company()
    contact["business_number"] = fake.phone()
    contact_list.append(contact)
return pd.DataFrame(contact_list)

# print(fake.name(), fake.email(), fake.travel_profession(), fake.company())


# people = [Meghan_Martin, Todd_Fuentes, Diana_Cummings, Tiffany_Camacho, Cody_Fletcher]


# def __str__(self):
# return f"{self.name} {self.surname} {self.email} {self.travel_profession} {self.company} "


# def __repr__(self):
# return f"Card(name={self.name} surname={self.surname}, email={self.email}, travel_profession={self.travel_profession}, company={self.company})"


# print(people)

# by_name = sorted(people, key=lambda Card: Card.name)
# lambda Card: Card.name
# print(by_name)
# by_surname = sorted(people, key=lambda Card: Card.surname)
# lambda Card: Card.surname
# print(by_surname)
# by_email = sorted(people, key=lambda Card: Card.email)
# lambda Card: Card.email
# print(by_email)


# def contact(self):
# return (
# f"Wybieram adres e-mail  {self.email} i piszę do {self.name} {self.surname}”."
# )
# @property
# def name_sum(self):
#   return self._name_sum

# @name_sum.setter
#   def name_sum(self, a):
#      a = (len(self.name) + len(self.surname))
#     self._name_sum = a


# print(Card())
# print(Cody_Fletcher.contact)
# def contact(self):
# return f"Wybieram numer {self.company_phone}{self.phone} i dzwonię do {self.name}{self.surname}”."
