from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Create SmartIT demo users"

    def handle(self, *args, **kwargs):

        # Admin user
        meena, created = User.objects.get_or_create(
            username="meena"
        )
        meena.set_password("Meena@123")
        meena.is_staff = True
        meena.is_superuser = True
        meena.save()

        # Employee user
        employee, created = User.objects.get_or_create(
            username="employee1"
        )
        employee.set_password("Employee@123")
        employee.is_staff = False
        employee.is_superuser = False
        employee.save()

        self.stdout.write(
            self.style.SUCCESS(
                "Demo users created/updated successfully!"
            )
        )