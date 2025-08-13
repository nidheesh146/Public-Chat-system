# filepath: /C:/Users/NIDHEESH/Desktop/Altos Work/chatbotproject/chatbotapp/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Message

def home(request):
    return render(request, 'home.html')


def chat(request):
    username = request.GET.get('username')
    room = request.GET.get('room', 'public')  # Default room is 'public'
    return render(request, 'chat.html', {'username': username, 'room': room})

def send_message(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        room = request.POST.get('room')
        content = request.POST.get('content')
        message = Message.objects.create(username=username, room=room, content=content)
        return JsonResponse({'message': message.content, 'username': message.username, 'timestamp': message.timestamp})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def get_messages(request, room):
    messages = Message.objects.filter(room=room).order_by('timestamp')
    return JsonResponse({'messages': [{'username': msg.username, 'content': msg.content, 'timestamp': msg.timestamp} for msg in messages]})

def enter(request):
    return render(request,'enter.html')

def company_login(request):
   
    return render(request, 'company_login.html')

def unemployed_login(request):
   
    return render(request, 'unemployed_login.html')

def company_registration(request):
    
    return render(request, 'company_reg.html')

def unemployed_registration(request):
   
    return render(request, 'unemployed_reg.html')

def admindash(request):
   
    return render(request, 'admindash.html')

def emp_dashboard(request):
   
    return render(request, 'emp_dashboard.html')



def chat_unemp(request):
    username = request.GET.get('username')
    room = request.GET.get('room', 'public')  # Default room is 'public'
    return render(request, 'chat_unemp.html', {'username': username, 'room': room})


def enter_unemp(request):
    return render(request,'enter_unemp.html')