

from django.shortcuts import render,redirect 
from first_app.forms import ToDoform
from first_app.models import ToDoModel

def home(request):
    return render(request, 'home.html')

def add_TODO(requset):
    if requset.method == 'POST':
        toDO = ToDoform(requset.POST)
        if toDO.is_valid():
            toDO.save(commit= True)
            
            return redirect('show_list')
    else :
        toDO = ToDoform()
        return render (requset, 'create_to_do.html',{'form': toDO})

def show_list(request):
    data = ToDoModel.objects.all()
    print(data)
    return render(request, 'show.html', {'data': data})


def edit_list(request, id):
    do_list = ToDoModel.objects.get(pk = id)
    do_form = ToDoform(instance=do_list)
    if request.method == "POST":
        do_form = ToDoform(request.POST, instance=do_list)
        if do_form.is_valid():
            do_form.save()
            return redirect('show_list')
    
    return render(request, 'create_to_do.html' , {'form' : do_form})

def delete (request,id):
    do_list = ToDoModel.objects.get(pk=id).delete()
    
    return redirect('show_list')


info = None
def completa(request,id): 
    # info = ToDoModel.objects.get(pk=id)
   
    do_list = ToDoModel.objects.get(pk = id).delete()
    return redirect('show_list')
  
def com(request):
    return render(request, 'complete.html',{'info': info})
