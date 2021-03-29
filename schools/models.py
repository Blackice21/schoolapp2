from django.db import models
# Create your models here.
class Principle(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    image = models.ImageField(default='nobody.jpg')

    def __str__(self):
        return self.first_name+' '+self.last_name

def get_principle():
    return Principle.objects.get_or_create(first_name='nobody',last_name='nobody', image='nobody.jpg')[0]

class School(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=7)
    image = models.ImageField(default='nobody.jpg')
    principle = models.ForeignKey(Principle, default=get_principle().id, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name