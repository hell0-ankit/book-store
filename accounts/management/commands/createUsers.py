from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Creates test/dummy users for book-store project"

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=5)
        parser.add_argument('--password', type=str, default='Test@1234')

    def handle(self, *args, **options):
        count = options['count']
        password = options['password']

        created_users = []

        for i in range(1, count + 1):
            email = f'testuser{i}@example.com'

            if User.objects.filter(username=email).exists():
                self.stdout.write(self.style.WARNING(f'{email} already exists, skipping'))
                continue

            User.objects.create_user(
                username=email,      # <-- ab username = email
                email=email,
                password=password,
                first_name=f'Test{i}',
            )
            created_users.append((email, password))

        self.stdout.write(self.style.SUCCESS(f'\nTotal {len(created_users)} users created successfully.\n'))
        self.stdout.write(self.style.SUCCESS(f"{'Email':<30}{'Password':<15}"))
        self.stdout.write('-' * 45)
        for email, pw in created_users:
            self.stdout.write(f"{email:<30}{pw:<15}")