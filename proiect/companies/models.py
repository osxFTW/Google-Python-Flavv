from django.db import models

from aplicatie1.models import Location


# Create your models here.
class Companies(models.Model):

    company_choices = (('SRL', 'S.R.L.'),
                       ('SA', 'S.A.'))

    name = models.CharField(max_length=100)
    website = models.CharField(max_length=50)
    company_type = models.CharField(max_length=5, choices=company_choices)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.company_type} {self.name} {self.website} {self.location}"
