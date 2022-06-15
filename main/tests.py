from django.test import TestCase
from .models import Reservation, Rental
from django.utils import timezone
# Create your tests here.

class RentalTests(TestCase):
    def test_create_rental(self):
        rental = Rental.objects.create(
        name='Global Ville')
        
        self.assertEqual(rental.name, 'Global Ville')
        
        
class ReservationTests(TestCase):
    def test_reservation(self):
        rental = Rental.objects.create(
        name='Global Ville')
        
        ##first reservation from today to checkout in 5 days
        checkin1 = timezone.now().date()
        checkout1 = timezone.now().date() + timezone.timedelta(days=5)
        reservation1 = Reservation.objects.create(rental=rental, checkin=checkin1, checkout=checkout1)
        
        ##first reservation from 5 days to checkout in another 5 days
        checkin2 = timezone.now().date() + timezone.timedelta(days=5)
        checkout2 = timezone.now().date() + timezone.timedelta(days=10)
        reservation2 = Reservation.objects.create(rental=rental, checkin=checkin2, checkout=checkout2)
        reservation_count = rental.reservations.count() 
        
        self.assertEqual(rental.name, 'Global Ville')
        self.assertEqual(reservation1.rental, rental)
        self.assertEqual(reservation1.checkin, checkin1)
        self.assertEqual(reservation1.checkout, checkout1)
        self.assertEqual(reservation_count, 2)