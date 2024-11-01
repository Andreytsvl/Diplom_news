from django.db import models

class Apteka(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Название аптеки")
    pharmacy_number = models.CharField(max_length=20, verbose_name="Номер аптеки")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    contact_number = models.CharField(max_length=15, verbose_name="Контактный телефон")

    class Meta:
        db_table = "apteka"
        verbose_name = "Аптека"
        verbose_name_plural = "Аптеки"

    def __str__(self):
        return self.name