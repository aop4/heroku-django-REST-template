from django.db import models
from django.conf import settings
from shortuuidfield import ShortUUIDField


# A useless example model
class Student(models.Model):
	uuid = ShortUUIDField(editable=False)
	name = models.CharField(max_length=100, default="")
	
	def __str__(self):
		return 'Student: ' + self.name



