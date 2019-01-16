from django.db import models
from isbn_field import ISBNField
from users.models import Member
from django.utils import timezone

# Create your models here.
class Book(models.Model):
	member = models.ForeignKey(Member, on_delete=models.PROTECT, default=1)
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=65)
	publisher = models.CharField(max_length=100)
	year = models.CharField(max_length=4)
	borrowed = models.DateTimeField(default=timezone.now)
	isbn = ISBNField()
	duration = models.DurationField()
	returned = models.BooleanField(default=0)

	def __str__(self):
		return self.title
