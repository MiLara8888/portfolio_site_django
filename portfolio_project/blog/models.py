from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    text=models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Блог'
        verbose_name_plural='Блог'


