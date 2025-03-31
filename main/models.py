from django.db import models


class UserMod(models.Model):
    user_id = models.PositiveBigIntegerField(verbose_name='telegram id')
    user_name = models.CharField(verbose_name='username', max_length=100)
    full_name = models.CharField(verbose_name='full name', max_length=150)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'


class AdminMod(models.Model):
    user_id = models.PositiveBigIntegerField(verbose_name='telegram id')
    user_name = models.CharField(verbose_name='foydalanuvchi ism', max_length=100, null=True, blank=True)
    full_name = models.CharField(verbose_name="to'liq ism", max_length=150)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Adminlar'