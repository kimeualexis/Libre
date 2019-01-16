from django.db import models
from isbn_field import ISBNField
from users.models import Member

# Create your models here.
class Book(models.Model):
	member = models.ForeignKey(Member, on_delete=models.PROTECT, default=1)
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=65)
	publisher = models.CharField(max_length=100)
	year = models.CharField(max_length=4)
	isbn = ISBNField()
	duration = models.DurationField()

	def __str__(self):
		return self.title
