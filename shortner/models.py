from django.db import models


class Link(models.Model):
    url = models.CharField("Link", max_length=1024)
    token = models.CharField("Short Url", max_length=200, unique=True)

    def __str__(self):
        return self.token
