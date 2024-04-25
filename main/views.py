from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse

from.models import todo
# Create your views here.


def todos(request):
    todos=todo.objects.all()
    return render(request,'home.html',{'todos':todos})

@require_http_methods(['POST'])
def add_todo(request):
    todoo=None
    title=request.POST.get('title','') 
    if title:
        todoo=todo.objects.create(title=title)
    return render(request,'list.html',{'todoo':todoo})


@require_http_methods(['PUT'])
def update_todo(request,pk):
    todoo=todo.objects.get(pk=pk)
    todoo.done =True
    todoo.save()
    return render(request,'list.html',{'todoo':todoo})
@require_http_methods(['DELETE'])
def delete_todo(request,pk):
    todoo=todo.objects.get(pk=pk)
    todoo.delete()
    return HttpResponse()