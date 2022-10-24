from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
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


def signUp(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Your account has been created. Please login')
            return redirect('loginPage')
    else:
        form = UserRegistrationForm()
    return render(request, 'datacenter/register.html' ,{'form': form})