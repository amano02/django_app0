from django.db import models

class SampleModel(models.Model):
  title=models.CharField(max_length=100)
  number=models.IntegerField()

CATEGORY = (('business','ビジネス'),('life','生活'),('other','その他'))
class Book(models.Model):
  title = models.CharField(max_length=100)
  text = models.TextField()
  category = models.CharField(
    max_length=100,
    choices=CATEGORY
  )

  def __str__(self):
    return self.title