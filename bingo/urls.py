from django.urls import path
from . import views


app_name = 'bingo'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('ticket/<str:username>/', views.TicketView.as_view(), name='ticket'),
    path('staff/', views.SearchView.as_view(), name='staff'),
    path('user-data/', views.user_json_data, name='user_json_data'),
    path('num/create/', views.add_num_to_db, name='num-create'),
    path('reset/', views.reset_game, name='reset'),

]
