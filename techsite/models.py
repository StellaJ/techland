from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50, blank=False)
    birth_date = models.DateField(blank=False)
    parents = models.CharField(max_length=100, blank=True)

    class Meta:
    	get_latest_by = "birth_date"

    def __unicode__(self):
        return self.name

# Create your models here.
