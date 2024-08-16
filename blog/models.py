from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    body = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='blog_previews/', verbose_name='превью')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    # признак публикации
    # количество просмотров

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
