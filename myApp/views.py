from django.shortcuts import render, redirect
from myApp.models import blogModel, portfolioModel
from myApp.forms import blogForm, portfolioForm

# Create your views here.

def blog(request):
    posts = blogModel.objects.all()[:4]
    return render(request, 'myApp/blog.html', {"posts": posts})

def contact(request):
    return render(request, 'myApp/contact.html')

def index(request):
    return render(request, 'myApp/index.html')

def portfolio(request):
    posts = portfolioModel.objects.all()[:10]
    images = [
        "myApp/img/portfolio-1.jpg",
        "myApp/img/portfolio-2.jpg",
        "myApp/img/portfolio-3.jpg",
        "myApp/img/portfolio-4.jpg",
        "myApp/img/portfolio-5.jpg",
        "myApp/img/portfolio-6.jpg",
        "myApp/img/portfolio-7.jpg",
        "myApp/img/portfolio-8.jpg",
        "myApp/img/portfolio-9.jpg",
        "myApp/img/portfolio-10.jpg",
    ]
    for post, image in zip(posts, images):
        post.image = image
    return render(request, 'myApp/portfolio.html', {"posts" : posts})

def formulaireBlog (request):
    if request.method == "POST":
        form = blogForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect("blog")
    else:
        form = blogForm()
    return render(request, "myApp/backoffice/formulaireBlog.html", {"form": form})

def formulairePort (request):
    if request.method == "POST":
        form = portfolioForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect("port")
    else:
        form = portfolioForm()
    return render(request, "myApp/backoffice/formulairePort.html", {"form": form})

