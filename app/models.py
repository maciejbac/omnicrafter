from django.db import models

class Customer(models.Model):
	item_id = models.CharField(max_length=200)

	def __str__(self):
		return self.item_id
