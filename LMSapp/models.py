from django.db import models

class Links(models.Model):
    title = models.TextField()
    link_url = models.TextField()

    def __str__(self):
        return u'%s %s' % (self.title, self.link_url)
