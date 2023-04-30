from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Coffee(models.Model):
    """Model representing a coffee drink."""
    type = models.ForeignKey('CoffeeType', on_delete=models.SET_NULL, null=True)

    # Foreign Key used because a coffee can only have one type, sizes are defined in another model
    size = models.ForeignKey('Size', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.type}, {self.size}'

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this coffee."""
        return reverse('coffee-detail', args=[str(self.id)])


class Size(models.Model):
    """Model representing a drink size."""
    name = models.CharField(max_length=50, unique=True, help_text="Enter a drink size (e.g. Small, Medium, Large)")

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        """Returns the URL to access a particular size instance."""
        return reverse('size-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.name
    

class CoffeeType(models.Model):
    """Model representing a type of coffee."""
    name = models.CharField(max_length=100, unique=True, help_text="Enter a coffee type (e.g. Latte, Filter, Cappuccino)")

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        """Returns the URL to access a particular coffee type instance."""
        return reverse('coffeetype-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.name

