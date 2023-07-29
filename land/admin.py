from django.contrib import admin
from .models import Property, Area, Image, Agency, LandTitle

class PropertyImageInline(admin.TabularInline):
    model = Image

class PropertyAdmin(admin.ModelAdmin):
    readonly_fields = ('reference_number',)
    def get_readonly_fields(self, request, obj=None):
        if obj:  # when editing an object
            return self.readonly_fields
        return ()  # when creating an object
    list_display = ( 'reference_number', 'title', 'description', 'price_thb')
    inlines = [PropertyImageInline]

admin.site.register(Property, PropertyAdmin)
admin.site.register(Area)
admin.site.register(Agency)
admin.site.register(LandTitle)