from django.shortcuts import render


# Create your views here.

def index(request):
    data = {
        'title' : 'Головна сторінка',
        'values' : ['Hello', 'World', 'Django', 'Python', 'HTML', 'CSS'],
        'obj' : {
            'model' : 'BMW',
            'color' : 'black',
            'doors' : 4,}
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')

    