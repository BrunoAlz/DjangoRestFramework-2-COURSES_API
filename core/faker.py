from faker import Faker

from django.contrib.auth.models import User

def populate(tipo, quantidade=0):
    """
        Popula a tabela de Usuários com o número de Usuários passados
    """
    fake = Faker()
    
    if tipo == 'Usuarios':
        for _ in range(quantidade):
            fn = fake.first_name()
            ln = fake.last_name()
            username = f'{fn}_{ln}'.lower()
            domain = fake.free_email_domain()
            email = f'{fn}_{ln}@{domain}'.lower()
            pass1 = '68210821Brn'

            user = User.objects.create(
                username=username,
                password=pass1,
                first_name=fn,
                last_name=ln,
                email=email                        
                )
            user.set_password(user.password)
            user.save()

        