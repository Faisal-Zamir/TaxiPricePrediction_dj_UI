from django.urls import path, include
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [

    path('notice/<int:pk>', views.NoticeDetailView.as_view(), name='notice-detail'),
    path('question/<int:pk>', views.QuestionDetailView.as_view(), name='question-detail'),
    path('profile/edit/<int:pk>', views.ProfileUpdateView.as_view(success_url="/college/mylist"), name='profile-update'),
    path('question/create/', views.QuestionCreate.as_view(success_url="/college/mylist")),
    path('',RedirectView.as_view(url='mylist/')),
    

    path('mylist/', views.MyList.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('', RedirectView.as_view(url="mylist/")),    
]
    #path('notice/', views.NoticeListView.as_view(), name='notice'),
