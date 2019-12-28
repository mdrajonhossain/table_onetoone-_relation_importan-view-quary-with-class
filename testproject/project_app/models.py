from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)


    def __str__(self):
    	return self.name

class Catagoryies(models.Model):
	person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="catagoryies")
	product_name = models.CharField(max_length=50)
	product_code = models.CharField(max_length=50)
	product_address = models.CharField(max_length=50)

	def __str__(self):
		return self.product_name
    