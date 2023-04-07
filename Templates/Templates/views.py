from django.shortcuts import render

def simples(request):
    return render(request, 'simples.html', {} )

def dinamico(request, name):
    categories = ['Code', 'Design', 'Marketing', 'Bussines', 'Data']
    contex = {'name': name, 'categories': categories}
    return render(request, 'dinamico.html', contex)