from django.shortcuts import render
from django.http import HttpResponse
from .models import NavbarModel, socialLinkModel, artLinkModel, artPhotosModel, softSkillsModel, progSkillsModel, Blog, Topic
from . import content

# rooms = [
#     {"id" : 1, 'name': 'israk'},
#     {'id': 2, 'name': 'Aklima'},
#     {'id': 3, 'name': 'Ridita'},
# ]

navs = NavbarModel.objects.all()
social_links = socialLinkModel.objects.all()
art_links = artLinkModel.objects.all()
art_photos = artPhotosModel.objects.all()
soft_skills = softSkillsModel.objects.all()
prog_skills = progSkillsModel.objects.all()
blogs = Blog.objects.all()
topics = Topic.objects.all()
blog_count = blogs.count()

#context
context = {
    'navs': navs,
    'socls': social_links,
    'art_links' : art_links,
    'art_photos' : art_photos,
    'soft_skills' : soft_skills,
    'prog_skills' : prog_skills,
    'blogs' : blogs,
    'topics' : topics,
    'blog_count' : blog_count,
}


# Create your views here.
def home(request):
    return render(request, 'home/home.html', context)


def about(request):
    return render(request, 'home/about.html', context)

def blog(request):
    return render(request, 'home/blog.html', context)
