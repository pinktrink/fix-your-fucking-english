from django.db import models


class Fix(models.Model):
    class Meta:
        app_label = 'fyfe'
        verbose_name_plural = 'fixes'

    title = models.CharField(max_length=128)
    description = models.TextField()
    supress_fixit_explanation = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title
