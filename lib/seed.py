#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game

fake = Faker()

if __name__ == '__main__':

    engine = create_engine('sqlite:///seed_db.db')
    Session = sessionmaker(bind=engine)
    session = Session()

session.query(Game).delete()
session.commit()

# botw = Game(title="Breath of the Wild", platform="Switch",
#             genre="Adventure", price=60)
# ffvii = Game(title="Final Fantasy VII",
#              platform="Playstation", genre="RPG", price=30)
# mk8 = Game(title="Mario Kart 8", platform="Switch", genre="Racing", price=50)
# grounded = Game(title="Grounded", platform="PC", genre="Survival", price=30)

games = [
    Game(
        title=fake.name(),
        platform=fake.word(),
        genre=fake.word(),
        price=random.randint(0, 60)
    )
    for i in range(50)
]

session.add_all(games)
session.commit()
