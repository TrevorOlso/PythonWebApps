from django.urls import path

from hero.views import MainView, HulkView, IronManView, BlackWidowView, AntManView, BlackPantherView

urlpatterns = [
    path('',        MainView.as_view()),
    path('hulk',        HulkView.as_view()),
    path('ironman', IronManView.as_view()),
    path('home', MainView.as_view()),
    path('blackwidow', BlackWidowView.as_view()),
    path('blackpanther', BlackPantherView.as_view()),
    path('antman', AntManView.as_view()),

]