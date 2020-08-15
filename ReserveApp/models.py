from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        """Meta definition for User."""

        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        """Unicode representation of User."""
        pass
# Create your models here.


class SoccerField(models.Model):
    TYPE_FIELD = [
        ('P','Pasto'),
        ('B','Baby'),
        ('G','Gimnacio')
    ]

    type_field = models.CharField(
        max_length=1,
        choices=TYPE_FIELD,
        default='P',
    )

    def getValue (self):
        if (self.type_field == 'P'):
            return 13000
        if (self.type_field == 'B'):
            return 10000
        else:
            return 8000

    class Meta:
        verbose_name = 'SoccerField'
        verbose_name_plural = 'SoccerFields'

    def __str__(self):
        return 'tipo: {type_field} valor: {value_type}'.format(
            value_type = self.getValue(),
            type_field = self.type_field,
        ) 

class Reserve(models.Model):
    user_name = models.CharField(max_length=50)
    field_name = models.ForeignKey('SoccerField', on_delete=models.CASCADE) 
    reserve_date = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        """Meta definition for Reserve."""

        verbose_name = 'Reserve'
        verbose_name_plural = 'Reserves'

    def __str__(self):
        return 'usuario:{user}- cancha: {field_name} - fecha:{reserve_date}'.format(
            user=self.user_name,
            field_name=self.field_name,
            reserve_date=self.reserve_date,
        )

