from django.db import models

# Create your models here.
class NavbarModel(models.Model):
    name = models.CharField(max_length=225)
    url = models.TextField(null= True, blank= True)
    def __str__(self):
        return self.name


class socialLinkModel(models.Model):
    name = models.CharField(max_length=225)
    icon = models.CharField(max_length=225)
    url = models.TextField(null= True, blank=True)
    def __str__(self):
        return self.name


class artLinkModel(models.Model):
    name = models.CharField(max_length=225)
    link = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name

class artPhotosModel(models.Model):
    name = models.CharField(max_length=225)
    src = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name

class softSkillsModel(models.Model):
    name = models.CharField(max_length=225)
    path = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name

class progSkillsModel(models.Model):
    name = models.CharField(max_length=225)
    path = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Blog(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.TextField(null=True, blank=True)
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    IDname = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.name