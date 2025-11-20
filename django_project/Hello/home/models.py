from django.db import models

# Create your models here.

#Makemigrations – create changes and store in a file
#Migrate - apply the panding changes created by makemigration

class Contact(models.Model):
    name =models.CharField(max_length=122)
    email =models.CharField(max_length=122)
    phone =models.CharField(max_length=12)
    desc =models.TextField()
    date = models.DateField()

    def __str__(self):
       return self.name