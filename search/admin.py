from django.contrib import admin
from django import forms
from search.models import Country,Region,Person,UnknownPerson
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.

class PersonAdminForm(forms.ModelForm):
    discription = forms.CharField(label="to'liq ma'lumot",widget=CKEditorUploadingWidget)
    class Meta:
        model = Person
        fields = "__all__"

class PersonAdmin(admin.ModelAdmin):
    form = PersonAdminForm

admin.site.register(Country)
admin.site.register(Region)
admin.site.register(UnknownPerson)
admin.site.register(Person,PersonAdmin)


