from django.db import models
# asd
# Create your models here.

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

    def __str__(self):
        return self.Qayerdan+"-"+self.Qayerga