from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='general'),
    path('about', views.about, name='about'),
    path('community', views.community, name='community'),
    path('profile', views.profile, name='profile'),
    path('login', views.login_in, name='login'),
    path('register', views.register, name='register'),
    path('create', views.create, name='create'),
    path('transactoin', views.transactoin, name='transactoin'),
    path('miner', views.miner, name='miner'),

]
