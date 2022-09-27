from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.shortcuts import resolve_url


class BasePersonModel(models.Model):
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'

    GENDER_CHOICES = (
        (GENDER_MALE, 'male'),
        (GENDER_FEMALE, 'female')
    )

    name = models.CharField(max_length=256)
    age = models.IntegerField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=100)
    born_at = models.DateField()
    # movies = models.ManyToManyField('Movie', related_name='actors')


    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Actor(BasePersonModel):
    def get_absolute_url(self):
        return resolve_url('actor_detail', pk=self.id)


class Director(BasePersonModel):
    def get_absolute_url(self):
        return resolve_url('director_detail', pk=self.id)


    # GENDER_MALE = 'male'
    # GENDER_FEMALE = 'female'
    #
    # GENDER_CHOICES = (
    #     (GENDER_MALE, 'male'),
    #     (GENDER_FEMALE, 'female')
    # )
    #
    # name = models.CharField(max_length=256)
    # age = models.IntegerField()
    # gender = models.CharField(choices=GENDER_CHOICES, max_length=100)
    # born_at = models.DateField()
    #
    # def __str__(self):
    #     return self.name


class Movie(models.Model):
    LANGUAGE_ENG = 'eng'
    LANGUAGE_CZ = 'cz'

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENG, 'english'),
        (LANGUAGE_CZ, 'czech'),
    )

    name = models.CharField(max_length=256)
    description = models.TextField()
    rating = models.IntegerField(validators=[
        MinValueValidator(0), MaxValueValidator(100)
    ])
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=5)
    released = models.DateField()
    actors = models.ManyToManyField('Actor', related_name='movies')
    director = models.ForeignKey(
        'Director',
        on_delete=models.SET_NULL,
        related_name='movies',
        null=True, blank=True
    )
    likes = models.IntegerField(default=0)

    # # mohu zmenit jmeno tridy 'Movies' na 'Filmy'
    # class Meta:
    #     verbose_name_plural = 'Filmy'

    def __str__(self):
        return f'{self.name} : {self.id}'

    def get_absolute_url(self):
        return resolve_url('movie_detail', pk=self.id)


class Contact(models.Model):
    name = models.CharField(max_length=37)
    email = models.EmailField()
    subject = models.TextField()
    phone_number = models.IntegerField()
    contact_at = models.DateField()

