from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

class AdditionalImage(models.Model):
    title = None
    bb = models.ForeignKey(Post, on_delete=models.CASCADE,
                            verbose_name='Объявление')
    image = models.ImageField( verbose_name='Изображение')
    
class Comment(models.Model):
    bb = models.ForeignKey(Post, on_delete=models.CASCADE,
                            verbose_name='Объявление')
    author = models.CharField(max_length=30, verbose_name='автор')
    content = models.TextField(verbose_name='Содержание')

