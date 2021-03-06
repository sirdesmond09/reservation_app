from django.db import models
from django.forms import model_to_dict

# Create your models here.
class Rental(models.Model):
    name = models.CharField(max_length=250, unique=True)
    date_added = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name
    
    
        
    

class Reservation(models.Model):
    rental = models.ForeignKey("main.Rental", on_delete=models.CASCADE, related_name="reservations")
    res_id = models.CharField(max_length=250, unique=True)
    checkin = models.DateField()
    checkout= models.DateField()
    
    class Meta:
        ordering = ['-pk']
    
    def __str__(self):
        return f"Reservation---{self.rental.name}-Checkin:--{self.checkin}"
    
    @property
    def prev_reservation(self):
        all_prev = Reservation.objects.filter(rental=self.rental, 
                                          pk__lt=self.id)
        
        if all_prev.exists():
            return all_prev.first().res_id
        return ""
    
    @property
    def rental_name(self):
        return self.rental.name