from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=12)
    slug = models.CharField(max_length=12)
    order = models.IntegerField(default=0)

    def __str__(self):
        return str(self.slug)


class Album(models.Model):
    category = models.OneToOneField(
        Category,
        on_delete=models.CASCADE,
    )
    cover = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return str(self.category.name) + " - album #" + str(self.id)


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    url = models.CharField(max_length=64)
    status = models.BooleanField(default=True)
    order = models.IntegerField(default=0) 

    def __str__(self):
        return "Album #" + str(self.album.id) + " - image #" + str(self.id)
