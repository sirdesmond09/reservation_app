from django.forms import model_to_dict
from django.test import TestCase
from .models import Reservation, Rental
from django.utils import timezone
from django.urls import reverse
from rest_framework.test import APITestCase
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
        reservation1 = Reservation.objects.create(res_id="Res-1",rental=rental, checkin=checkin1, checkout=checkout1)
        
        ##second reservation from 5 days to checkout in another 5 days
        checkin2 = timezone.now().date() + timezone.timedelta(days=5)
        checkout2 = timezone.now().date() + timezone.timedelta(days=10)
        reservation2 = Reservation.objects.create(res_id="Res-2",rental=rental, checkin=checkin2, checkout=checkout2)
        
        
        ##third reservation from 10 days to checkout in another 5 days
        checkin3 = timezone.now().date() + timezone.timedelta(days=15)
        checkout3 = timezone.now().date() + timezone.timedelta(days=20)
        reservation3 = Reservation.objects.create(res_id="Res-3",rental=rental, checkin=checkin3, checkout=checkout3)
        reservation_count = rental.reservations.count() 
        
        self.assertEqual(rental.name, 'Global Ville')
        self.assertEqual(reservation1.rental, rental)
        self.assertEqual(reservation1.checkin, checkin1)
        self.assertEqual(reservation1.checkout, checkout1)
        self.assertEqual(reservation_count, 3)
        self.assertEqual(reservation1.prev_reservation, "")
        self.assertEqual(reservation2.prev_reservation, reservation1.res_id)
        self.assertEqual(reservation3.prev_reservation, reservation2.res_id)
        
        
        
class ViewTest(APITestCase):
    
    def setUp(self):
        rental = Rental.objects.create(name='Global Ville')
        
        ##first reservation from today to checkout in 5 days
        checkin1 = timezone.now().date()
        checkout1 = timezone.now().date() + timezone.timedelta(days=5)
        reservation1 = Reservation.objects.create(res_id="Res-1",rental=rental, checkin=checkin1, checkout=checkout1)
        
        ##second reservation from 5 days to checkout in another 5 days
        checkin2 = timezone.now().date() + timezone.timedelta(days=5)
        checkout2 = timezone.now().date() + timezone.timedelta(days=10)
        reservation2 = Reservation.objects.create(res_id="Res-2",rental=rental, checkin=checkin2, checkout=checkout2)
    
    def test_view_returns_OK(self):
        response = self.client.get(reverse('main:reservation'))
        self.assertEqual(response.status_code,200)


    def test_view_returns_correct_data(self):
        response = self.client.get(reverse('main:reservation'))  
        data = [{
                   
                    "prev_reservation":"Res-1",
                    "res_id":"Res-2",
                    "checkin":"2022-06-21",
                    "checkout":"2022-06-26",
                    "rental_name":'Global Ville'
            },
                
                {
                    "prev_reservation":"",
                    "res_id":"Res-1",
                    "checkin":"2022-06-16",
                    "checkout":"2022-06-21",
                    "rental_name":'Global Ville'
            }
        ]
        self.assertJSONEqual(str(response.content, encoding='utf8'),data)

