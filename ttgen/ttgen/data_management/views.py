from django.shortcuts import render

# Create your views here.

def dataManagement(request):
    return render(request, 'data_management/base2.html')




def addCourse(request):
    return render(request, 'data_management/course.html')


def addProfessor(request):
    return render(request, 'data_management/professor.html')


def daysTime(request):
    return render(request, 'data_management/days-time.html')


def rooms(request):
    return render(request, 'data_management/rooms.html')