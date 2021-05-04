from django.http import JsonResponse

# Create your views here.

data ={
    'Name' : 'Kelvin Tagoe',
    'Track' :'Backend(Python)',
    'Message' : 'Hi,mentor,I appreciate the time and effort,you are doing an amazing job.'
}

def index(request):
    return JsonResponse(data)
