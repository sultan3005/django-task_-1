from django.shortcuts import render
from.models import Post
from django.core.mail import send_mail
from django.conf import settings

def main_page(request):
    return render(request, 'base.html')


def about(request):
    with open('posts/texts/about_as.txt', 'r') as file:
        data = file.read()
    return render(request, 'about.html', {'data': data})

def gallery(request):
    posts = Post.objects.all()
    return render(request, 'gallery.html', {'posts': posts})

def contact(request):
    with open('posts/texts/contact.txt', 'r') as file:
        data = file.read()
    return  render(request, 'contact.html', {'data':data})


def index(request):
    if request.method == "POST":
        massage = request.POST['message']

        send_mail('contact user:', massage, settings.EMAIL_HOST_USER,
                  ['7504515@gmail.com'],
                  fail_silently=False)

    return render(request, 'base.html')