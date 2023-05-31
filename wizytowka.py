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


class Card:
    def __init__(self, name, surname, company, position, email):
        self.name = name
        self.surname = surname
        self.company = company
        self.position = position
        self.email = email


# Derek_Coon = Card(
# name="Derek",
# surname="Coon",
# company="K&G Distributors",
# position="Network architect",
# email="DerekJCoon@dayrep.com",
# )
# print(Card)
for _ in range(5):
    print(fake.name(), fake.email(), fake.travel_profession(), fake.company())
