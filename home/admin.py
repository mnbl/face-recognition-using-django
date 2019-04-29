from django.contrib import admin
from home.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display=(
        'face_id',
        'name',
        'phone',
        'job',
        'email',
        'address',
    )

admin.site.register(UserProfile, UserProfileAdmin)