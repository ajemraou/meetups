from django.db import models

# Create your models here.

class Location(models.Model):
  name = models.CharField(max_length=100)
  address = models.CharField(max_length=200)

  def __str__(self):
    return f'{self.name}, ({self.address})'

class Participant(models.Model):
  email = models.EmailField(unique=True)


  def __str__(self):
    return self.email

class Meetup(models.Model):
  title = models.CharField(max_length=200)
  organizer_email = models.EmailField()
  description = models.TextField()
  location = models.ForeignKey(Location, on_delete=models.CASCADE)
  date = models.DateTimeField()
  slug = models.SlugField(unique=True)
  image = models.ImageField(upload_to='images')
  Participant = models.ManyToManyField(Participant, blank=True, null=True )

  def __str__(self):
    return self.title