from django.shortcuts import render

from core.faker import populate

def core_index(request):
    template_name = 'core/core_index.html'
    
    # populate('Usuarios', 30)

    context = {

    }

    return render(request, template_name, context)
