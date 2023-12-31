from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from .models import Student, Teacher, Subject


# Create your views here.
class MyHomeView(TemplateView):
    template_name = 'first_app/home.html'

class StudentListView(ListView):
    # model _list.html -> student_list.html
    model = Student  # Connected to Models Student
    queryset = Student.objects.order_by('name')  # Result ordered by name
    context_object_name = 'students'  # default object_list now students
    paginate_by = 10 # 10 per page in ListView


class StudentDetailView(DetailView):
    # Return only one model entry
    # default template model_detail.html => student_default.html
    model = Student

class StudentCreateView(CreateView):
    template_name = 'first_app/student_form_create.html'
    model = Student
    fields = '__all__'  # All fields into form
    success_url = reverse_lazy('first_app:student_list')

class StudentUpdateView(UpdateView):
    #  model_form.html => student_form.html
    model = Student
    fields = ['name', 'weight']  # update only this field
    success_url = reverse_lazy('first_app:student_list')

class StudentDeleteView(DeleteView):
    # Form -> Confirm Delete Button
    # default template name => model_confirm_delete.html ->
    # -> student_confirm_delete.html
    model = Student
    # redirect after successful delete
    success_url = reverse_lazy('first_app:student_list')

class TeacherListView(ListView):
    model = Teacher
    queryset = Teacher.objects.order_by('name')

class TeacherCreateView(CreateView):
    # template_name = 'first_app/teacher_form_create.html'
    model = Teacher
    fields = '__all__'  # All fields into form
    success_url = reverse_lazy('first_app:teacher_list')

class SubjectListView(ListView):
    model = Subject
    queryset = Subject.objects.order_by('subject')
    context_object_name = 'subjects'

class SubjectDetailView(DetailView):
    model = Subject

class SubjectCreateView(CreateView):
    template_name = 'first_app/subject_form_create.html'
    model = Subject
    fields = '__all__'
    success_url = reverse_lazy('first_app:subject_list')

class SubjectUpdateView(UpdateView):
    #  model_form.html => student_form.html
    model = Subject
    fields = '__all__'  # update only this field
    success_url = reverse_lazy('first_app:subject_list')

class SubjectDeleteView(DeleteView):
    model = Subject
    success_url = reverse_lazy('first_app:subject_list')