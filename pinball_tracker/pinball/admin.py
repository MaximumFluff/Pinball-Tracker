from django.contrib import admin
from .models import Score

admin.site.site_header = "Pinball Tracker"
admin.site.index_title = "Admin Dashboard"
admin.site.register(Score)
