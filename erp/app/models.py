from django.db import models

# Create your models here.
class Staff(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class Shift(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name

class Entry(models.Model):

    staff = models.ForeignKey(Staff,on_delete=models.CASCADE)
    date = models.DateField()
    shift = models.ForeignKey(Shift,on_delete=models.CASCADE)
    entry = models.IntegerField()
    errors = models.IntegerField()
    comments = models.TextField()

    class Meta:
        unique_together = ('staff', 'date')

