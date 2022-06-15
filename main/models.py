from django.db import models

# Create your models here.
class Rental(models.Model):
    name = models.CharField(max_length=250, unique=True)
    date_added = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name
    

class Reservation(models.Model):
    rental = models.ForeignKey("main.Rental", on_delete=models.CASCADE, related_name="reservations")
    checkin = models.DateField()
    checkout= models.DateField()
    
    
    def __str__(self):
        return f"Reservation---{self.rental.name}-Checkin:--{self.checkin}"