from django.db import models


class Editor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s %s" % (self.first_name, self.last_name)

    class Meta:
        verbose_name='Editor'
        verbose_name_plural = 'Editors'


class Reporter(models.Model):
    profession = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s %s" % (self.profession, self.first_name,
                             self.last_name)

    class Meta:
        verbose_name='Reporter'
        verbose_name_plural = 'Reporters'


class Publisher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        verbose_name='Publisher'
        verbose_name_plural = 'Publishers'
