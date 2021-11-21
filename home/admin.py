from django.contrib import admin
from .models import NavbarModel, socialLinkModel, artLinkModel, artPhotosModel, softSkillsModel, progSkillsModel, Blog, Topic

# Register your models here.
admin.site.register(NavbarModel)
admin.site.register(socialLinkModel)
admin.site.register(artLinkModel)
admin.site.register(artPhotosModel)
admin.site.register(softSkillsModel)
admin.site.register(progSkillsModel)
admin.site.register(Topic)
admin.site.register(Blog)