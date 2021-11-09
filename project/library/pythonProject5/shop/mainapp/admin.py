from django.forms import ModelChoiceField, ModelForm, ValidationError
from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
# Register your models here.
from .models import *

from PIL import Image

class NotebookAdminForm(ModelForm):



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            """"<span style="color:red; font-size: 14px;">При загрузке изображения с разрешением больше максимального {}x{} оно будет обрезано!</span>""".format(
                *Product.MAX_RESOLUTION))



    #def clean_image(self):
        #image = self.cleaned_data['image']
        #img = Image.open(image)
        #min_height, min_width = Product.MIN_RESOLUTION
        #max_height, max_width = Product.MAX_RESOLUTION
        #f image.size > Product.MAX_IMAGE_SIZE:
        #    raise ValidationError('Размер изображения не должен превышать 3MB')
        #if img.height < min_height or img.width < min_width:
        #    raise ValidationError('Разрешение изображение меньше минимального')
        #if img.height > max_height or img.width > max_width:
        #    raise ValidationError('Разрешение изображение больше максимального')
        #return image



class NotebookAdmin(admin.ModelAdmin):

    form = NotebookAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name =='category':
            return ModelChoiceField(Category.objects.filter(slug='notebooks'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SmartphoneAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name =='category':
            return ModelChoiceField(Category.objects.filter(slug='smartphones'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



admin.site.register(Category)
admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Smartphone,SmartphoneAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
