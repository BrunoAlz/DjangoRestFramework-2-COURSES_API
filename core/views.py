from django.shortcuts import render

def core_index(request):
    template_name = 'core/core_index.html'

    context = {

    }

    return render(request, template_name, context)
