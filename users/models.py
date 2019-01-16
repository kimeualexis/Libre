from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Member(models.Model):
	fname = models.CharField(max_length=30)
	sname = models.CharField(max_length=30)
	dob = models.DateTimeField(default=timezone.now)
	school = models.CharField(max_length=100)
	level = models.CharField(max_length=30)
	zone = models.CharField(max_length=100)
	contact = models.CharField(max_length=100, default='0712345677')
	joined = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.fname

	def get_absolute_url(self):
		return reverse('users:libre-index')
		

