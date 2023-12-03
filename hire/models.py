from django.db import models
from catering.models import Allergen

# Creates chef hire package
class HirePackage(models.Model):
    """
    Model for the Hire packages
    """
    package_name = models.CharField(max_length=254)
    description = models.TextField()
    serves_nr_guests = models.TextField(blank=True, null=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True,)
    hires = models.ManyToManyField('HireRequest', blank=True)

    def __str__(self):
        return self.package_name


# Creates Hire possibility for user
class HireRequest(models.Model):
    hire_package = models.ForeignKey(HirePackage, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    date = models.DateField()
    time = models.TimeField()
    nr_of_guests = models.IntegerField()
    allergies = models.ManyToManyField(Allergen, blank=True)
    comments = models.TextField()
    replied = models.BooleanField(default=False)