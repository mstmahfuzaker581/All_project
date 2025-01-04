from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
instruments_choices = [('Guitar', 'Guitar'),
                       ('Drum', 'Drum'), ('Flute', 'Flute')]

# Create your models here.


class Musician(models.Model):
    first_name = models.CharField(
        max_length=255, error_messages="Name can't be more than 255 characters")
    last_name = models.CharField(
        max_length=255, error_messages="Name can't be more than 255 characters")
    email = models.EmailField(
        unique=True, error_messages="Email must be unique and valid")
    phone_number = models.CharField(
        max_length=11, error_messages="Phone number must be 11 digits")
    instrument = models.CharField(max_length=50, choices=instruments_choices)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} "


class Album(models.Model):
    album_name = models.CharField(max_length=255)
    release_date = models.DateField(auto_now_add=True)
    rating = models.FloatField(
        validators=[MaxValueValidator(5.0), MinValueValidator(0.0)])
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.album_name}"