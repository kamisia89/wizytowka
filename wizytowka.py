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
    def __init__(self, name, surname, email, travel_profession, company):
        self.name = name
        self.surname = surname
        self.email = email
        self.profession = travel_profession
        self.company = company


# for _ in range(5):
# print(fake.name(), fake.email(), fake.travel_profession(), fake.company())
Meghan_Martin = Card(
    "Meghan", "Martin", "alexander29@example.org", "tour manager", "Gallegos-Williams"
)
Todd_Fuentes = Card(
    "Todd",
    "Fuentes",
    "raymond26@example.com",
    "tourist guide",
    "Bowen Sanford and Huerta",
)
Diana_Cummings = Card(
    "Diana", "Martn", "kathryn73@example.org", "travel agent", "Hancock and Sons"
)
Tiffany_Camacho = Card(
    "Tiffany", "Camacho", "frichard@example.com", "tourist guide", "Moore Group"
)
Cody_Fletcher = Card(
    "Cody", "Fletcher", "amberdunn@example.com", "hotel manager", "Russell Inc"
)
card = Card()
# by_name = sorted(Card, key=lambda Card: Card.name)
print(card())
