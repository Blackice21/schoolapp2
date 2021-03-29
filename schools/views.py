from django.shortcuts import render, redirect, get_object_or_404
from .models import School
from .forms import Schoolform
# Create your views here.
def home(request):
    schools = School.objects.all()
    return render(request, 'home.html',{'schools': schools})

def Create_school(request):
    if request.method == 'GET':
        form = Schoolform
        return render(request, 'create_school.html', {'form': form})
    else:
        form = Schoolform(request.POST, request.FILES)
        form.save()
        return redirect('home')

def detail_school(request, pk):
    school = get_object_or_404(School, pk=pk)
    return render(request, 'detail_school.html',{'school':school})

def update_school(request, pk):
    school = get_object_or_404(School, pk=pk)
    if request.method == "GET":
        schoolform = Schoolform(instance=school)
        return render(request, "update_school.html",{'schoolform':schoolform, 'school':school}) 

    else:
        schoolform = Schoolform(request.POST, request.FILES, instance=school)
        schoolform.save()
        return redirect('home')

def delete_school(request, pk):
        school = get_object_or_404(School,pk=pk)
        school.delete()
        return redirect('home')

def search(request):
    schools = School.objects
    search_info = request.GET['search_info']
    searched_schools = schools.filter(name__icontains=search_info)
    return render(request, 'search.html', {'searched_schools': searched_schools, 'search_info': search_info})