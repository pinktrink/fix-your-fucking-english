from django.db import models

from fyfe.models import Fix


class Search(models.Model):
	class Meta:
		app_label = 'fyfe'
		verbose_name_plural = 'searches'
	
	fix = models.ForeignKey(Fix)
	word = models.CharField(max_length=16)
