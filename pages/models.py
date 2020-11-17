from django.db import models

# Create your models here.
class Pages(models.Model):
	title = models.CharField(max_length=50)
	link = models.CharField(unique=True, max_length=50)
	body = models.TextField('Page content', blank=True)
	update_date = models.DateTimeField('Last Updated', blank=True)

	def __str__(self):
		return self.title