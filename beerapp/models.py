from django.db import models

# User Model
'''class User(models.Model):
	username = models.CharField(max_length=40)
	password = models.CharField(max_length=100)
	
	def __str__(self):
		return self.username'''
	
# Beer Model
class Beer(models.Model):
	ibu = models.IntegerField(null=False)
	calories = models.IntegerField(null=False)
	abv = models.FloatField(default=None)
	style = models.CharField(max_length=100,default=None)
	brewery_location = models.CharField(max_length=300,default=None)
	

class Review(models.Model):
	aroma = models.IntegerField(null=False)
	appearance = models.IntegerField(null=False)
	taste = models.IntegerField(null=False)
	
	def overall(self):
		average = (self.aroma + self.appearance + self.taste)/3