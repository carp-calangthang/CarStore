from django.contrib import admin
from product.models import *
from django.utils.safestring import mark_safe

class CarModelAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'car_company', 'car_price', 'car_color', 'car_quantity', 'upload_date')
    readonly_fields = ('display_image',)

    def display_image(self, obj):
        return mark_safe(f'<img src="{obj.car_images.url}" width="500" height="auto" style="border-radius: 10px;" />')

    display_image.short_description = 'Car Image'
    
class AccessaryAdmin(admin.ModelAdmin):
    list_display = ('accessary_name', 'accessary_company', 'accessary_price', 'accessary_quantity', 'upload_date')
    readonly_fields = ('display_image',)

    def display_image(self, obj):
        return mark_safe(f'<img src="{obj.accessary_images.url}" width="500" height="auto" style="border-radius: 10px;" />')

    display_image.short_description = 'Accessary Image'
    
admin.site.register(car_model, CarModelAdmin)
admin.site.register(Accessary, AccessaryAdmin)
