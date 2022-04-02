from django.db import models

class Kunyomi(models.Model):
    kunyomi = models.CharField(max_length=50)

class Onyomi(models.Model):
    onyomi = models.CharField(max_length=50)

class Meaning(models.Model):
    meaning = models.CharField(max_length=255)

class Kanji(models.Model):
    symbol = models.CharField(max_length=10)
    jlpt = models.IntegerField()
    kunyomis = models.ManyToManyField(Kunyomi, related_name='kanji_kunyomi')
    onyomis = models.ManyToManyField(Onyomi, related_name='kanji_onyomi')
    meanings = models.ManyToManyField(Meaning, related_name='kanji_meaning')