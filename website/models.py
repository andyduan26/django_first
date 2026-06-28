from django.db import models


class Contract(models.Model):
    name = models.CharField(max_length=120, blank=True, default='')
    email = models.EmailField(max_length=254, blank=True, default='')
    whatsapp = models.CharField(max_length=60, blank=True, default='')
    requirement = models.TextField(blank=True, default='')

    class Meta:
        db_table = 'contract'
        verbose_name = '联系表单'
        verbose_name_plural = '联系表单'

    def __str__(self):
        return self.name or f'Contract #{self.pk}'
