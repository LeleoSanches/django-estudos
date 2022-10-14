from unittest.util import _MAX_LENGTH
from django.db import models
import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='publicado')


class Post(models.Model):
    STATUS = (
        ('rascunho','Rascunho'),
        ('publicado','Publicado'),
        ('zoado','Zoado'),
        ('fornicado','Fornicado'),
    )
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    conteudo = models.TextField()
    publicado = models.DateTimeField(default=timezone.now)
    criado = models.DateTimeField(auto_now_add=True)
    alterado = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS,default='rascunho')
    


    objects = models.Manager()
    published = PublishedManager()
    class Meta:
        ordering = ('-publicado',)

    def __str__(self):
        return '{} - {} '.format(self.titulo,self.slug)