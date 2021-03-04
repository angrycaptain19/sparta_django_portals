from django.contrib import admin
from accounts.models import User, Participant, LocalGovUnit
# Register your models here.
admin.site.register(User)
admin.site.register(Participant)
admin.site.register(LocalGovUnit)
