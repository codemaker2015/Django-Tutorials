from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name=models.CharField(max_length=260,unique=True)
    def __str__(self):
        return self.top_name
class WebPage(models.Model):
    catagory=models.ForeignKey(Topic, on_delete=models.CASCADE)
    name=models.CharField(max_length=264)
    url=models.URLField()
    def __str__(self):
        return self.name
class AccessRecord(models.Model):
    name2=models.ForeignKey(WebPage, on_delete=models.CASCADE)
    date=models.DateField()
    def __str__(self):
        return str(self.date)
