from django.shortcuts import render

def lista_servicos(request):
    return render(request, 'sistema/servicos.html')

def agendar(request):
    return render(request, 'sistema/agendar.html')

def agendamento_sucesso(request):
    return render(request, 'sistema/sucesso.html')
