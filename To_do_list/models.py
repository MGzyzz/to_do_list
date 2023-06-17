from django.db import models


class Task(models.Model):

    TASK_STATUS_CHOICE = (
        ('new', 'Новая'),
        ('in_progress', 'В процессе'),
        ('done', 'Сделано')
    )

    description = models.TextField(
        max_length=1000,
        null=False,
        blank=False,
        verbose_name="Описание"
    )
    status = models.CharField(
        max_length=20,
        choices=TASK_STATUS_CHOICE,
        default='new',
        null=False,
        blank=False
    )

    date_of_completion = models.DateField(
        "Дата выполнение",
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.status}: {self.date_of_completion}'
# Create your models here.
