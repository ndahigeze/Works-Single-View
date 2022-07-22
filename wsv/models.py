from django.db import models

# Create your models here.


class WorkMetadata(models.Model):
    title = models.CharField(max_length=250,null=False, blank=False)
    iswc = models.CharField(max_length=250, null=True, blank=True)


class Contributor(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    metadata = models.ForeignKey(WorkMetadata, on_delete=models.CASCADE)



