# encoding: utf-8
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms.extras.widgets import SelectDateWidget

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.db.models import Q
from django import forms
from django.contrib import messages

from blog.models import Post
# from blog.forms import StudentModelForm, StudentAddForm



class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    # paginate_by = 3

    def get_queryset(self):
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            posts = Post.objects.filter(courses__id=course_id).order_by('id')
        else:
            posts = Post.objects.all().order_by('-create_date')



        # q = self.request.GET.get("q")
        # if q:
        #     posts = posts.filter(
        #         Q(name__icontains=q) |
        #         Q(surname__icontains=q)
        #         )

        return posts


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        post = self.get_object()

        return context


    # def get_context_data(self, **kwargs):
    #     context = super(StudentListView, self).get_context_data(**kwargs)

    #     if not self.object_list:
    #         context['messages'] = [u"Не найдено студентов по запросу '{}'.".format(self.request.GET.get("q"))]
    #         # for i in context:
    #         #     print '--->', i
    #     return context



# class StudentCreateView(CreateView):
#     model = Student
#     success_url = reverse_lazy('students:list_view')
#     form_class = StudentAddForm

#     def get_context_data(self, **kwargs):
#         context = super(StudentCreateView,self).get_context_data(**kwargs)
#         context['title'] = 'Student registration'
#         return context

#     def form_valid(self, form):
#         application = form.save()
#         msg = u"Student %s %s has been successfully added." % (
#             application.name, application.surname)
#         messages.success(self.request, msg)
#         return super(StudentCreateView, self).form_valid(form)


# class StudentUpdateView(UpdateView):
#     model = Student
#     template_name_suffix = '_update_form'
#     success_url = reverse_lazy('students:edit')
#     form_class = StudentAddForm

#     def get_context_data(self, **kwargs):
#         context = super(StudentUpdateView, self).get_context_data(**kwargs)
#         context['title'] = u"Student info update"
#         return context

#     def get_success_url(self):
#         return reverse_lazy('students:edit', args=(self.object.id,))

#     def form_valid(self, form):
#         application = form.save()
#         messages.success(
#             self.request, u"Info on the student has been sucessfully changed.")
#         return super(StudentUpdateView, self).form_valid(form)


# class StudentDeleteView(DeleteView):
#     model = Student
#     template_name_suffix = '_delete_form'
#     success_url = reverse_lazy('students:list_view')

#     def get_context_data(self, **kwargs):
#         context = super(StudentDeleteView, self).get_context_data(**kwargs)
#         context['title'] = u"Student info suppression"
#         context['notice'] = u"Студент %s %s будет удален" % (
#             self.object.name, self.object.surname)
#         return context

#     def delete(self, request, *args, **kwargs):
#         messages.success(
#             self.request, 'Info on {} has been sucessfully deleted.'.format(self.get_object()))
#         return super(StudentDeleteView, self).delete(self, request, *args, **kwargs)

