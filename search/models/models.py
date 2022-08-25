from django.db import models
from ckeditor.fields import RichTextField

class Country(models.Model):
    name = models.CharField("mamlakat", max_length=100, help_text="Mamlakatni kiriting:")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "mamlakat"
        verbose_name_plural = "mamlakatlar"


class Region(models.Model):
    name = models.CharField("viloyat", max_length=100, help_text="Viloyatni kiriting:")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "viloyat"
        verbose_name_plural = "viloyatlar"


class Person(models.Model):
    first_name = models.CharField("ismi", max_length=100, help_text="Shaxs ismini kiriting:")
    last_name = models.CharField("familiya", max_length=100, help_text="Shaxs familiyasini kiriting:")
    age = models.PositiveIntegerField("yoshi", help_text="Shaxs yoshini kiriting:")
    image = models.ImageField("sur'at",upload_to='images/', help_text="Shaxs sur'atini yuklang:")
    discription = RichTextField("to'liq ma'lumot",help_text="to'liq izoh kiritng:")
    country = models.ForeignKey(Country, verbose_name="mamlakat", null=True, on_delete=models.SET_NULL)
    region = models.ForeignKey(Region, verbose_name="viloyat", null=True, on_delete=models.SET_NULL)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "shaxs"
        verbose_name_plural = "shaxslar"

class UnknownPerson(models.Model):
    image = models.ImageField(upload_to='unkimages/', help_text="Shaxs sur'atini yuklang:")     #, related_name = "unkimage"