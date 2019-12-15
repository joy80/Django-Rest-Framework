from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.

class Profile(models.Model):
	file = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
	name = models.CharField(max_length=50,blank=True, null= True,)
	email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
	phone = models.CharField(max_length=20,default=0,blank=True, null= True,)
	skill = models.TextField(blank=True, null= True,)

	def __str__(self):
		return self.name
	
