from django.db import models




class country(models.Model):
    country = models.CharField(max_length=25, default='USA')

    def __str__(self):
        return self.country

class house(models.Model):
    country = models.ForeignKey(country, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    price = models.IntegerField(default=25)
    inventory = models.IntegerField(default=25)
    expense = models.IntegerField(default=0)
    owned = models.BooleanField(default='False')

    def __str__(self):
        return str(self.country)+' - '+str(self.name)

class player(models.Model):
    name = models.CharField(max_length=250)
    country = models.ForeignKey(country, on_delete=models.CASCADE, default='USA')
    cash = models.IntegerField(default=2000)
    debt = models.IntegerField(default=2200)
    health = models.IntegerField(default=100)
    inventory = models.IntegerField(default=25)
    house = models.CharField(max_length=50, default='Homeless')

    def __str__(self):
        return self.name


class drug(models.Model):
    country = models.ForeignKey(country, on_delete=models.CASCADE)
    name = models.CharField(max_length=5)
    price = models.CharField(max_length=25)


    def __str__(self):
        return str(self.country)+' - '+str(self.name)

class store(models.Model):
    country = models.ForeignKey(country, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    price = models.IntegerField(default=25)
    description = models.CharField(max_length=250, default="none")