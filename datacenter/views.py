from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

datas = [
    {
        'agent_id': 100, 
        'agent_name': 'Kimani', 
        "location": "Nairobi"
    },
    {
        'agent_id': 101, 
        'agent_name': 'John', 
        "location": "Nairobi"
    },
]

def homePage(request):
    '''
    Function to view homepage
    '''
    context = {
        "datas": datas
    }
    return render(request, 'datacenter/home.html', context)