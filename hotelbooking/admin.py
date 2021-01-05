from django.contrib import admin

# Register your models here.
# Register your models here.

from hotelbooking.models import Customer,Room,AccessRecord
admin.site.register(Customer)
admin.site.register(Room)
admin.site.register(AccessRecord)