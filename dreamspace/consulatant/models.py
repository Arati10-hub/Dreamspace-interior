from django.db import models
# Create your models here.


class ConsultationRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)
    date = models.DateField()
    time_slot = models.CharField(max_length=50, choices=[
        ('09:00 AM - 10:00 AM', '09:00 AM - 10:00 AM'),
        ('10:00 AM - 11:00 AM', '10:00 AM - 11:00 AM'),
        ('02:00 PM - 03:00 PM', '02:00 PM - 03:00 PM'),
        ('03:00 PM - 04:00 PM', '03:00 PM - 04:00 PM'),
    ])

    def _str_(self):
        return f"{self.name} - {self.date} ({self.time_slot})"