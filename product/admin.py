from django.contrib import admin

# Register your models here.
from .models  import Product ,ProductImage,Product_Alternative,Product_Accessories
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Product_Alternative)
admin.site.register(Product_Accessories)
