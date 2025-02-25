from django.contrib import admin

# Register your models here.

from . models import wedding_card
admin.site.register(wedding_card)

admin.site.site_header = 'SadiCard Administration'  # Changes the header on the admin page
admin.site.site_title = 'SadiCard Admin Portal'     # Changes the browser tab title
admin.site.index_title = 'Welcome to Card Management System'  # Changes title on admin index page
