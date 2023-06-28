from django.db import models



class Status(models.Model):
    name = models.CharField(
        max_length=200,
        null=False,
        blank=None,
        verbose_name='Имя'
    )

    def __str__(self):
        return self.name



class Task(models.Model):
    #
    name = models.CharField(
        max_length=250,
        null=True,
        blank=False,
        verbose_name='Имя'
    )

    description = models.TextField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name="Описание"
    )

    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    start_date = models.DateField(
        'Начало даты',
        null=True,
        blank=True
    )

    date_of_completion = models.DateField(
        "Дата выполнение",
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.status}: {self.date_of_completion}'
# Create your models here.
