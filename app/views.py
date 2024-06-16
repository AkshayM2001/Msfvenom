# views.py
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
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
