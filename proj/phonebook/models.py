from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255, verbose_name="Contact name")

    def __str__(self):
        return f"{self.name}"


class Phone(models.Model):
    phone = models.CharField(max_length=100, verbose_name="Phone")
    contact = models.ForeignKey(Person,
                                on_delete=models.CASCADE,
                                related_name="phones")

    def __str__(self):
        return self.phone
