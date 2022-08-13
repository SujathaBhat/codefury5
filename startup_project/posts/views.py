from django.shortcuts import render

posts = [
    {
        'author': 'Siri',
        'title': 'Post',
        'content': 'First post content',
        'date_posted': 'August 7, 2021'
    },
    {
        'author': 'tom',
        'title': 'jerry',
        'content': 'Hi',
        'date_posted': 'August 14, 2021'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'posts/home.html', context)


def about(request):
    return render(request, 'posts/about.html', {'title': 'About'})