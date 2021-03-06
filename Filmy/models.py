from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Genre name",
                            help_text='Enter a film genre (drama, sci-fi, horror)')

    class Meta:
        ordering = ["name"]

    def __str__(self):
        """ Řetězec, který se používá jako textová reprezentace objektu (například v
       administraci aplikace).
        V našem případě bude objekt (žánr) reprezentován výpisem obsahu pole name """
        return self.name

class Film(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    plot = models.TextField(blank=True, null=True, verbose_name="Plot")
    release_date = models.DateField(blank=True, null=True,
                                    help_text="Please use the following format: <em>YYYY-MM-DD</em>.",
                                    verbose_name="Release date")
    runtime = models.IntegerField(blank=True, null=True,
                                  help_text="Please enter an integer value (minutes)",
                                  verbose_name="Runtime")
    rate = models.FloatField(default=5.0,
                             validators=[MinValueValidator(1.0), MaxValueValidator(10.0)],
                             null=True, help_text="Please enter an float value (range 1.0 - 10.0)",
                             verbose_name="Rate")
    genres = models.ManyToManyField(Genre, help_text='Select a genre for this film')

    class Meta:
        ordering = ["-release_date", "title"]

    def __str__(self):
        """Součástí textové reprezentace filmu bude jeho název, rok uvedení a hodnocení"""
        return f"{self.title}, year: {str(self.release_date.year)}, rate: {str(self.rate)}"

    def get_absolute_url(self):
        """Metoda vrací URL stránky, na které se vypisují podrobné informace o filmu"""
        return reverse('film-detail', args=[str(self.id)])