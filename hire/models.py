from django.db import models


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

    def __str__(self):
        return self.package_name