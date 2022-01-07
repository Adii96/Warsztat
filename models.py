from django.db import models

class Sala(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.IntegerField()
    availability = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {self.capacity} {self.availability}"

class Reserve(models.Model):
    date = models.DateField()
    comment = models.TextField(null=True)
    id_room = models.ForeignKey(Sala, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('id_room', 'date',)


# Create your models here.
