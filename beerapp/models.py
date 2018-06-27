from django.db import models

from django.core.exceptions import ValidationError

def validate_only_one_instance(obj):
	model = obj.__class__
	if (model.objects.count() > 0 and
			obj.id != model.objects.get().id):
			raise ValidationError("Can only create 1 beer instance per day.")

	
# Beer Model
class Beer(models.Model):
	name = models.CharField(max_length=100,default=None)
	ibu = models.IntegerField(null=False)
	calories = models.IntegerField(null=False)
	abv = models.FloatField(default=None)
	style = models.CharField(max_length=100,default=None)
	brewery_location = models.CharField(max_length=300,default=None)
	
	def __str__(self):
		return self.name
		
	def clean(self):
		validate_only_one_instance(self)
	

class Review(models.Model):
	beer = models.ForeignKey(Beer, on_delete=models.CASCADE, default=None)
	aroma = models.IntegerField(null=False)
	appearance = models.IntegerField(null=False)
	taste = models.IntegerField(null=False)
	
	def overall(self):
		average = (((self.aroma / 5) * 100)  + ((self.appearance  / 5) * 100) + ((self.taste / 5) * 100))/3
		
		return average