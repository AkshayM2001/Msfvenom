# views.py
from django.http import JsonResponse, HttpResponse,HttpRequest,request
from django.views.decorators.csrf import csrf_exempt
import json
import socket
from .models import SMSData
from django.shortcuts import render

@csrf_exempt
def receive_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            sender = data.get('sender')
            message = data.get('message')
            
            # Save data to the database
            SMSData.objects.create(sender=sender, message=message)
            
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        return HttpResponse(status=405)  # Method Not Allowed
    

def display_data(request):
    data = SMSData.objects.all()
    return render(request, 'display_data.html', {'data': data})

def test_connection(request):
    return JsonResponse({'status': 'success', 'message': 'Connection successful!'})



def start_listener(request):
    HOST = '216.24.57.4'  # Listen on all network interfaces
    PORT = 80  # Choose a port to listen on

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)  # Listen for one incoming connection

        response = f'Listening on {HOST}:{PORT}\n'

        conn, addr = s.accept()
        with conn:
            response += f'Connected by {addr}\n'
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                # Handle the received data here
                response += f'Received: {data.decode()}\n'

    return HttpResponse(response)

