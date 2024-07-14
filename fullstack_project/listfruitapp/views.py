from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def index(request):
    fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
    students = Student.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm()

    context = {
        'fruits': fruits,
        'students': students,
        'form': form,
    }
    return render(request, 'listfruitapp/index.html', context)
