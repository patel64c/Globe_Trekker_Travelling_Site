from django.db import models
from django.core.validators import FileExtensionValidator
from collections import namedtuple

from django.utils.safestring import mark_safe
# Create your models here.
class login_table(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=10)
    phone_no=models.IntegerField()
    ROLE=(
        ("admin","admin"),
        ("agent","agent"),
        ("user","user")
    )
    role=models.CharField(max_length=10,choices=ROLE)
    STATUS=(
        ("0","INACTIVE"),
        ("1","ACTIVE")
    )
    status =models.CharField(max_length=10,choices=STATUS)

    def __str__(self):
        return self.email

class country(models.Model):
    country_name=models.CharField(max_length=25)

    def __str__(self):
        return self.country_name


class state_table(models.Model):
    state_name=models.CharField(max_length=25)
    country_id =models.ForeignKey(country,on_delete=models.CASCADE)

    def __str__(self):
        return self.state_name


class city_table (models.Model):
    city_name=models.CharField(max_length=25)
    state_id=models.ForeignKey(state_table,on_delete=models.CASCADE)
    def __str__(self):
        return self.city_name


class detail_table(models.Model):
    login_id =models.ForeignKey(login_table,on_delete=models.CASCADE)
    name=models.CharField(max_length=25)
    dob =models.DateField()
    display_pic=models.ImageField(upload_to="photos")
    address = models.CharField(max_length=50)
    city_id=models.ForeignKey(city_table,on_delete=models.CASCADE)
    state_id = models.ForeignKey(state_table,on_delete=models.CASCADE)
    country_id=models.ForeignKey(country,on_delete=models.CASCADE)

    def admin_photos(self):
       return mark_safe('<img src="{}" width="100"/>'.format(self.display_pic.url))

    admin_photos.allow_tags = True

    def __str__(self):
        return self.name 

class package_type_table(models.Model):
    type_name =models.CharField(max_length=25)

    def __str__(self):
        return self.type_name

class package_details(models.Model):
    login_id =models.ForeignKey(login_table,on_delete=models.CASCADE)
    package_name =models.CharField(max_length=20)
    type_id = models.ForeignKey(package_type_table,on_delete=models.CASCADE)
    package_image =models.ImageField(upload_to="photos")
    p_status = (
        ("open", "open"),
        ("closed", "closed"),
    )
    package_status = models.CharField(max_length=50, choices=p_status, default="open")
    status_button = models.BooleanField(default=False)
    no_of_day =models.IntegerField()
    package_description =models.TextField()
    package_price=models.IntegerField()
    Package_date=models.DateField(null=True)

    def admin_image(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.package_image.url))

    admin_image.allow_tags = True

    def admin_video(self):
        return mark_safe('< source video "{}" width="100"/>'.format(self.package_video.url))
    admin_video.allow_tags = True



    def __str__(self):
        return self.package_name

class booking_details(models.Model):
    booking_name = models.CharField(max_length=50, default='Test')
    no_of_adults = models.CharField(max_length=50, default='5')
    no_of_child = models.CharField(max_length=50, default='1')
    From = models.CharField(max_length=50, default='1')
    Departure_date = models.DateField(null=True)
    login_id =models.ForeignKey(login_table,on_delete=models.CASCADE)
    status=(
        ("pending","pending"),
        ("confirmed","confirmed"),
        ("cancelled","cancelled")
    )
    booking_status = models.CharField(max_length=10,choices=status)
    package_data = models.ForeignKey(package_details,on_delete=models.CASCADE, null=True)

    Payment_status=(
        ('pending','pending'),
        ('successful','successful'),
    )
    payment_status=models.CharField(max_length=10,choices=Payment_status, default="pending")
    datetime=models.DateTimeField(auto_now=True,editable=False)
    time =models.TimeField(auto_now=True,editable=False)


class feedback(models.Model):
    login_id=models.ForeignKey(login_table,on_delete=models.CASCADE)
    ratings=models.CharField(max_length=300, default="")
    comment=models.CharField(max_length=300, default="")

class contactform(models.Model):
    name=models.CharField(max_length=50,default="")
    email=models.EmailField(default="")
    comment=models.CharField(max_length=250,default="")




class card_detail(models.Model):
    name=models.CharField(max_length=50)
    card_number=models.CharField(max_length=50)
    card_cvv=models.CharField(max_length=50)
    exp_date=models.CharField(max_length=50)
    card_balance=models.IntegerField(default=1000000)

    def __str__(self):
        return self.card_number