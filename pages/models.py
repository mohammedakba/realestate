from django.db import models

# Create your models here.


class RegisterUser(models.Model):
    name = models.CharField(max_length=100)
    phno = models.CharField(max_length=100)


class Uploadproperty(models.Model):
    id = models.AutoField
    property_cat = models.CharField(choices=(('Home', 'Home'), ('Appartment', 'Appartment'), (
        'Building', 'Building'), ('Land', 'Land'), ('Farm House', 'Farm House'), ('Banglow', 'Banglow')), max_length=15)
    property_type = models.CharField(
        choices=(('Sell', 'Sell'), ('Rent', 'Rent')), max_length=10)
    project_name = models.CharField(max_length=20)
    description = models.TextField()
    price = models.FloatField(default=0)
    image = models.ImageField(
        upload_to="pages/images", default='No Image')
    image1 = models.ImageField(
        upload_to="pages/images", default='No Image')
    image2 = models.ImageField(
        upload_to="pages/images", default='No Image')
    image3 = models.ImageField(
        upload_to="pages/images", default='No Image')
    image4 = models.ImageField(
        upload_to="pages/images", default='No Image')
    contact_PersonName = models.CharField(max_length=20)
    contact_Number = models.CharField(max_length=12)
    contact_email = models.EmailField(
        max_length=50)

    def __str__(self):
        return self.property_cat
