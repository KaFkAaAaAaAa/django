from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.


#                               TWORZENIE TABELI BAZODANOWEJ

# definiujemy klase Post która dziedziczy po klasie models obiektu model
class Post(models.Model):
    # tworzenie kolumny tytuł o maksymalnej długości 250 znaków
    title = models.CharField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Opublikowany")
    )

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")

    # slug - unikatowy identyfikator dla ścieżki
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")

    class Meta:
        ordering = ("-publish",)

    # metoda toString() w pythonie
    def __str__(self):
        return self.title
