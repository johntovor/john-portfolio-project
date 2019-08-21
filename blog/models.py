from django.db import models
from datetime import datetime


class MyBlog(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    pub_date = models.DateField(default=datetime.now, blank=True)

    def summary(self):
        return self.body[:100] + "..."

    def __str__(self):
        return self.title
