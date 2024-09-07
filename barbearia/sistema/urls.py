from django.urls import path
from . import views

urlpatterns = [
    path('servicos/', views.lista_servicos, name='lista_servicos'),
    path('agendar/', views.agendar, name='agendar'),
    path('sucesso/', views.agendamento_sucesso, name='agendamento_sucesso'),
]
