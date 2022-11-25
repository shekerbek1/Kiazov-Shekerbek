from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm

def about(request):
    return render(request, 'my_list/home.html')

def mane(request):
    u = Articles.objects.all()

    return render(request, 'my_list/mane.html', {'data': u})

def index(request):
    return render(request, 'my_list/about.html')



def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/mane')
        else:
            error = 'Форма было неверной'
    form = ArticlesForm()
    data = {
        'form': form,
        'erorr': error
    }

    return render(request, 'my_list/main.html', data)



