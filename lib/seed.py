#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Dev, Company, Freebie


engine = create_engine('sqlite:///lib/freebies.db')


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()



company1 = Company(name="safaricom", founding_year=2004)
company2 = Company(name="Google", founding_year=1998)


dev1 = Dev(name="Billy")
dev2 = Dev(name="Kelvin")


session.add_all([company1, company2, dev1, dev2])
session.commit()


freebie1 = Freebie(item_name="laptop", value=50000, company=company1, dev=dev1)
freebie2 = Freebie(item_name="Stickers", value=500, company=company1, dev=dev2)

session.add_all([freebie1, freebie2])
session.commit()

print("Seed testing complete")

