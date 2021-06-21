from django.contrib import admin
from .models import category,product


# Register your models
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(category,CategoryAdmin)




class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','category','stock','available','created','updated']
    list_editable = ['price','stock','available']
    list_per_page = 20
    prepopulated_fields = {'slug':('name',)}

admin.site.register(product,ProductAdmin)