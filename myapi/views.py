import io
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from myapi.serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer


# Create your views here.
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        
        if serializer.is_valid():
            serializer.save()
            res = {'msg', 'Data Created'}
            json_data = JSONRenderer().render(data=res)
            return HttpResponse(json_data, content_type='application/json')
        
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')