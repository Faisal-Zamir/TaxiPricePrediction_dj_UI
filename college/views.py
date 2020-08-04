from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView
from . models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http.response import HttpResponseRedirect


# @method_decorator(login_required, name="dispatch") 
# class NoticeListView(ListView):
#     model = Notice
#     def get_queryset(self):
#         search_q = self.request.GET.get('search_query')
#         if search_q ==None:
#             search_q = ""
#         if self.request.user.is_superuser:
#             return Notice.objects.filter(Q(subject__icontains = search_q) | Q(msg__icontains = search_q) ).order_by('-id')
#         else:
#             return Notice.objects.filter(Q(branch = self.request.user.profile.branch) | Q(branch__isnull=True)).filter(Q(subject__icontains = search_q) | Q(msg__icontains = search_q)).order_by("-id")
           



# @method_decorator(login_required, name="dispatch") 
# class NoticeListView(ListView):
#     model = Notice
#     def get_queryset(self):
#         if self.request.user.is_superuser:
#             return Notice.objects.order_by('-id')
#         else:
            
#             return Notice.objects.filter(Q(branch = self.request.user.profile.branch) | Q (branch__isnull = True)).order_by("-id")
#             # return Notice.objects.filter(branch=self.request.user.profile.branch).order_by('-id')
      




@method_decorator(login_required, name="dispatch") 
class NoticeDetailView(DetailView):
    model = Notice


@method_decorator(login_required, name="dispatch")    
class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ["branch", "sem", "marks_10", "marks_12", "marks_aggr", "rn", "myimg", "myresume", "skills"]

@method_decorator(login_required, name="dispatch")    
class QuestionCreate(CreateView):
    model = Question
    fields = ["subject", "msg"]
    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())



class MyList(TemplateView):
    template_name = "college/home.html"
    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        context["notices"] = Notice.objects.order_by("-id")[:3]
        context["questions"] = Question.objects.order_by("-id")[:3]
        return context

@method_decorator(login_required, name="dispatch") 
class QuestionDetailView(DetailView):
    model = Question



# def home(req):
#     return render(req, "college/home.html", {"name":'Faisal'})

def about(req):
    return render(req, "college/about.html",{"name":'Ali'})

def contact(req):
    return render(req, "college/contact.html",{"name":'AMIR'})
