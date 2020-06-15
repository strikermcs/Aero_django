from django.shortcuts import render
from django.http import HttpResponse

from .models import Main_win, my_skills, my_services 

def my_first_simple_view(request):
    return render(
        request,
        'pages/index.html',
        {
            "Main": Main_win.objects.get(id = 1),
            "skills": my_skills.objects.all(),
            "services": my_services.objects.all(),
        }
    )
