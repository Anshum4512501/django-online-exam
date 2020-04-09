from django.db import models

# Create your models here.

# class Company(models.Model):
    # name = models.CharField(max_length=100)
    # employee = models.M

class Emplyoee(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

# class Activity(models.Model):
#     start_date = models.DateTimeField()
#     end_date = models.DateTimeField()
    

# class Throttle(models.Model):
#     ok = models.BooleanField(default=True)
#     members = models.ForeignKey(Members,on_delete=models.CASCADE)
# class
#  Members(models.Model):
#     id = models.CharField(max_length = 6,primary_key = True)
#     real_name = models.CharField(max_length=100)
#     tz = models.CharField(max_length=100)
#     activity = models.ForeignKey(Activity,on_delete=models.CASCADE)


class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline