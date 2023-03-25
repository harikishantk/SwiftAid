from django.db import models
from webcampicture.fields import WebcamPictureField


# Create your models here.

class Notification(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    

    def __str__(self):
        return self.title

class Location(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

class HelpRequest(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'PENDING'),
        ('ACCEPTED', 'ACCEPTED'),
        ('COMPLETED', 'COMPLETED'),
    )

    TYPES_CHOICES = (
        ('FOOD', 'FOOD'),
        ('MEDICINE', 'MEDICINE'),
        ('CLOTHES', 'CLOTHES'),
        ('SHELTER', 'SHELTER'),
        ('RESCUE', 'RESCUE'),
        ('MISSING', 'MISSING'),
        ('OTHER', 'OTHER'),

    )
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES, default='PENDING', max_length=100)
    description = models.CharField(max_length=100)
    type = models.CharField(choices=TYPES_CHOICES,max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    picture = WebcamPictureField(
        "Picture", upload_to="images/", blank=False
    )

    def __str__(self):
        return self.user.username + ' ' + self.type + ' ' + self.status
    