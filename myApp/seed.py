from django_seed import Seed
from myApp.models import blogModel, portfolioModel
# import random
import faker

def run():
    seeder = Seed.seeder()
    fake = faker.Faker()
    seeder.add_entity(blogModel, 4, {
        'titre' : lambda x: seeder.faker.sentence(nb_words=3),
        'image' : lambda x: seeder.faker.image_url(),
        'description' : lambda x: seeder.faker.text()
    })
    seeder.add_entity(portfolioModel, 10, {
        'titre' : lambda x: seeder.faker.sentence(nb_words=3),
        'description' : lambda x: seeder.faker.text()
    })
    inserted_pks = seeder.execute()
    print(inserted_pks)
