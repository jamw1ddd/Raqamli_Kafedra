from django.contrib import admin
from .models import StaffMember, Post, ContactMessage

admin.site.register(StaffMember)
admin.site.register(Post)
admin.site.register(ContactMessage)