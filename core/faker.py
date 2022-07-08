from faker import Faker

from django.contrib.auth.models import User

def populate(n=0):

    for _ in range(n):
        fake = Faker()
        fn = fake.first_name()
        ln = fake.last_name()
        username = f'{fn}_{ln}'
        domain = fake.free_email_domain()
        url = fake.url()
        email = f'{fn}_{ln}@{domain}'

        pass1 = '131288Brn'
        pass2 = '131288Brn'

        User.objects.get_or_create(
            username=username,
            first_name=fn,
            last_name=ln,
            email=email,            
            )


def avaliacao_populate(n=0):

    for _ in range(n):
        pass
        