from django.shortcuts import render
from django.http import  HttpResponse 
from app.models import Student


# def home (request):
#     data=Student.objects.create(
#         Name='priya',
#         City='kghl',
#         Email='priya@gmail.com',
#         Contact='741963'
#     )
#     print(data)
#     return HttpResponse(data)


# def home(request):
#     data= Student.objects.first()

#     print(data.Name)
#     print(data.City)
#     print(data.Contact)
#     print(data.Email)
        
    
#     return HttpResponse(data)


                        #    COMPOSITE QUERY  
                        # means using queryset in multiple
# def home(request):
#     data= Student.objects.all()[::-2]
#     print(data)
#     return HttpResponse(data)

# def home(request):
#     data=Student.objects.get(id=2).delete()
#     print(data)
#     return HttpResponse(data)

# def home(request):
#     data=Student.objects.filter(Name='mehak').delete()
#     print(data)
#     return HttpResponse(data)

def home(request):
    data=Student.objects.filter(Name='priya').update(Name='pihu')
    print(data)
    return HttpResponse(data)

# def home(request):
#     data= Student.objects.order_by('Name')
#     print(data)
#     return HttpResponse(data)