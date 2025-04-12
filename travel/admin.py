from django.contrib import admin
from .models import login_table
from .models import  country
from .models import state_table
from .models import city_table
from .models import detail_table
from .models import package_type_table
from .models import package_details
from .models import booking_details
from .models import feedback
from .models import contactform
from .models import card_detail



# Register your models here.
class LOGIN(admin.ModelAdmin):
    list_display = ["email","phone_no","password","role","status"]
admin.site.register(login_table,LOGIN)

class Country(admin.ModelAdmin):
    list_display = ["country_name"]
admin.site.register(country,Country)

class State_table(admin.ModelAdmin):
    list_display = ["state_name","country_id"]
admin.site.register(state_table,State_table)

class City_table(admin.ModelAdmin):
    list_display = ["city_name","state_id"]
admin.site.register(city_table,City_table)

class Detail(admin.ModelAdmin):
    list_display = ["login_id","name","dob","admin_photos","address","city_id","state_id","country_id"]
admin.site.register(detail_table,Detail)

class Package_Type_table(admin.ModelAdmin):
    list_display = ["id","type_name"]
admin.site.register(package_type_table,Package_Type_table)

class Package_Details(admin.ModelAdmin):
    list_display = ["login_id","package_name","type_id","admin_image","package_status","status_button","no_of_day","package_description","package_price","Package_date"]
admin.site.register(package_details,Package_Details)

class Card_Detail(admin.ModelAdmin):
    list_display = ["name","card_number","card_cvv","exp_date","card_balance"]
admin.site.register(card_detail,Card_Detail)


class Booking_Details(admin.ModelAdmin):
    list_display = ["login_id","no_of_adults","no_of_child","From","Departure_date","booking_status","payment_status","datetime","time"]
admin.site.register(booking_details,Booking_Details)

class Feedback(admin.ModelAdmin):
    list_display = ["login_id","ratings","comment"]
admin.site.register(feedback,Feedback)

class Conatctform(admin.ModelAdmin):
    list_display = ["name","email","comment"]
admin.site.register(contactform,Conatctform)



