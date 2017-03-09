from django.db import models
from writer.models import Reporter, Editor, Publisher


class Publication(models.Model):
    title = models.CharField(max_length=30)
    editors=models.ForeignKey(Editor, on_delete=models.CASCADE)

    def __str__(self):              # __unicode__ on Python 2
        return self.title

    class Meta:
        verbose_name='Subject'
        verbose_name_plural = 'Subjects'


class Article(models.Model):
    headline = models.CharField(max_length=100)
    text = models.TextField(max_length=500)
    publications = models.ManyToManyField(verbose_name='Subject',
                                          to='Articles.Publication')
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, verbose_name='Reporter')

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)
        verbose_name='Article'
        verbose_name_plural = 'Articles'

    def publications_name(self):
        return self.publications.get(pk=self.pk)


class Magazine(models.Model):
    magazine_name=models.CharField(max_length=50)
    publisher=models.ForeignKey(Publisher,verbose_name='Publisher')
    pubs=models.ManyToManyField(Publication, verbose_name='Subject')
    arts=models.ManyToManyField(Article,verbose_name='Article')

    class Meta:
        verbose_name='Magazine'
        verbose_name_plural = 'magazines'

    def __str__(self):
        return self.magazine_name


# Create your models here.
