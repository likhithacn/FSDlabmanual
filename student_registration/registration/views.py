from django.shortcuts import render, redirect
from .models import Student, Course, Enrollment
from .forms import StudentForm, EnrollmentForm

def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_student')
    else:
        form = StudentForm()
    return render(request, 'register_student.html', {'form': form})

def enroll_student(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enroll_student')
    else:
        form = EnrollmentForm()
    return render(request, 'enroll_student.html', {'form': form})

def course_students(request, course_id):
    course = Course.objects.get(id=course_id)
    enrollments = Enrollment.objects.filter(course=course)
    students = [enrollment.student for enrollment in enrollments]
    return render(request, 'course_students.html', {'course': course, 'students': students})

# module4
from django.views.generic import ListView, DetailView
class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'  # Specify template for rendering student list
    context_object_name = 'students'  # Specify context variable name for the student queryset

class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'  # Specify template for rendering student detail
    context_object_name = 'student'  # Specify context variable name for the student object
