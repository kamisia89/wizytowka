from faker import Faker

f = Faker("en_GB")
f = Faker()
# from faker.providers import DynamicProvider

# import pandas as pd

# travel_professions_provider = DynamicProvider(
#   provider_name="travel_profession",
#  elements=[
#     "hotel manager",
#    "cruise ship steward",
#   "cabin crew",
#  "tourist guide",
# "tour manager",
# "travel agent",
# "sailing instructor",
# ],
# )

# fake.add_provider(travel_professions_provider)


class BaseContact:
    def __init__(
        self,
        first_name,
        last_name,
        phone_number,
        email,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.name = 0


class BusinessContact(BaseContact):
    def __init__(self, job, company, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job = job
        self.company = company
        self.business_phone = business_phone


"""
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
    """
if __name__ == "__main__":
    person_1 = BaseContact(
        first_name="Robert",
        last_name="Kelly",
        phone_number=9726397253,
        email="blairlarry@example.com",
    )
person_2 = BaseContact(
    first_name="Jaime",
    last_name="Reese",
    phone_number=9726397253,
    email="amurphy@example.net",
)
person_3 = BaseContact(
    first_name="Debra",
    last_name="Mason",
    phone_number=7435350260,
    email="ulynn@example.net",
)
person_4 = BaseContact(
    first_name="Jon",
    last_name="Padilla",
    phone_number=7654563239,
    email="nancywolfe@example.net",
)
person_5 = BaseContact(
    first_name="Sarah",
    last_name="Bell",
    phone_number=7769866745,
    email="crystal74@example.com",
)

persons = (
    person_1,
    person_2,
    person_3,
    person_4,
    person_5,
)


def __str__(self):
    return f"{self.first_name}{self.last_name}{self.phone_number}{self.email})"


print(persons)


def __repr__(self):
    return f"BusinessContact(bussiness_phone={self.business_phone}, first_name={self.first_name}, last_name={self.last_name})"


def contact(self):
    return f"Wybieram numer {self.business_phone}{self.phone_number} i dzwonię do {self.first_name}{self.last_name}”."

    # basic = BaseContact()

    # TO PSUJE CALY KOD => card = Card()

    # def contact(self):
    #   return f"{self.name}{self.surname}


# def create_contacts(num_contacts):
#   contact_list = []


# for _ in range(5):
#   contact = {}
#  contact["name"] = fake.name()
# contact["last_name"] = fake.last_name()
# contact["phone_number"] = fake.phone_number()
# contact["email"] = fake.email()
# contact["role"] = fake.random_element(
# elements=(
#   "Hotel Manager",
#    "Travel Agent",
#    "Tour Operator",
#   "Tourist Guide",
#   "Tour Manager",
#   "Sailing Instructor",
# )
# )

# contact["company"] = fake.company()
#  contact["business_number"] = fake.phone_number()
#   contact_list.append(contact)
#  return pd.DataFrame(contact_list)


@property
def name_lenght(self):
    self.name_lenght = len(self.first_name) + len(self.slast_name)
    #print(self.name_lenght)
    return self.name_lenght
 for i in persons:
    print((first_name)(last_name), name_lenght)



by_first_name = sorted(persons, key=lambda BaseContact: BaseContact.first_name)
lambda BaseContact: BaseContact.first_name
print(by_first_name)
by_last_name = sorted(persons, key=lambda BaseContact: BaseContact.last_name)
lambda BaseContact: BaseContact.last_name
print(by_last_name)
by_email = sorted(persons, key=lambda BaseContact: BaseContact.email)
lambda BaseContact: BaseContact.email
print(by_email)


# num_contact = input(f"Ile kontaktów?")

# create_contacts = 5

# print(fake.name(), fake.email(), fake.travel_profession(), fake.company())


# people = [Meghan_Martin, Todd_Fuentes, Diana_Cummings, Tiffany_Camacho, Cody_Fletcher]


# def __str__(self):
# return f"{self.name} {self.surname} {self.email} {self.travel_profession} {self.company} "


#
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
