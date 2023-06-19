from django.db import models
from django.contrib.auth.models import User


car_choices = (
    ("Cobalt", "Cobalt"),
    ("Nexia 3", "Nexia 3"),
    ("Lacetti", "Lacetti"),
    ("Jentra", "Jentra"),
    ("Nexia 2", "Nexia 2"),
    ("Malibu", "Malibu"),
    ("Epika", "Epika"),
    ("Spark", "Spark"),
    ("Nexia 1", "Nexia 1"),
    ("Malibu", "Malibu"),
    ("Malibu 2", "Malibu 2"),
    ("Kaptiva", "Kaptiva"),
    ("Onix", "Onix"),
    ("Matiz", "Matiz"),
    ("Damas", "Damas"),
    ("boshqa model", "boshqa model"),
)

class Profile(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    ism = models.CharField(max_length=255)
    familiya = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    car_model = models.CharField(max_length=255, choices=car_choices, verbose_name = "Avtomobil modeli")
    plate_number = models.CharField(max_length=255, verbose_name = "Avtomobil raqami") # namuna kiritib qo'y 80 A180BB

    def __str__(self):
        return self.ism+" "+self.familiya

Viloyat_choices = (
    ("Toshkent sh", "Toshkent sh"),
    ("Toshkent", "Toshkent"),
    ("Qashqadaryo", "Qashqadaryo"),
    ("Surxandaryo", "Surxandaryo"),
    ("Andijon", "Andijon"),
    ("Farg'ona", "Farg'ona"),
    ("Namangan", "Namangan"),
    ("Sirdaryo", "Sirdaryo"),
    ("Jizzax", "Jizzax"),
    ("Samarqand", "Samarqand"),
    ("Navoiy", "Navoiy"),
    ("Buxoro", "Buxoro"),
    ("Qoraqalpog'iston AR", "Qoraqalpog'iston AR"),
)


class Taklif(models.Model):
    Qayerdan = models.CharField(max_length=255, choices=Viloyat_choices)
    Qayerga = models.CharField(max_length=255, choices=Viloyat_choices)
    Orinlar_soni = models.IntegerField(verbose_name = "Bo'sh o'rinlar soni")
    Kun = models.DateField()
    Narx = models.IntegerField()
    Vaqt = models.TimeField()
    Author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Qayerdan+"-"+self.Qayerga

