from django.shortcuts import render
from django.http import HttpResponse

navs = [
    {"name": 'Home', 'url': '/'},
    {"name": 'About', 'url': 'about'},
    {"name": 'Blog', 'url': 3},
    {"name": 'Artwork', 'url': 4},
]
social_links = [
    {'icon': 'fab fa-facebook-f', 'url': '/'},
    {'icon': 'fab fa-instagram', 'url': '/'},
]
photos = [
    {'cover': 'https://cdn.pixabay.com/photo/2018/01/14/23/12/nature-3082832__340.jpg'},
]

#context
context = {
    'navs': navs,
    'socls': social_links,
    'photos' : photos,
}
# Create your views here.
def home(request):
    return render(request, 'home/home.html', context)


def about(request):
    return render(request, 'home/about.html', context)
