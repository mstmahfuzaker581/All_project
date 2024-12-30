from django.shortcuts import render
from .forms import ContactForm
from .forms import passwordValidationProject
from .forms import StudentData
def home(request):
    return render(request, 'home.html')

def about(request):
    if request.method == "POST": 
       print(request.POST)
       username = request.POST.get('username')
       email = request.POST.get('email')
       select= request.POST.get('select')
       return render(request, 'about.html', {"username": username, "email": email, "select": select})
    else:
     return render(request, 'about.html')

def submit_form(request): 
    return render(request, 'form.html')

def DjangoForm(request):
    if request.method=="POST":
        form=ContactForm(request.POST,request.FILES)
        if form.is_valid():
           file=form.cleaned_data['file']
           with open('upload/' + file.name,'wb+') as destination:
               for chunk in file.chunks():
                    destination.write(chunk)
           print(form.cleaned_data)
           return render(request,'django_form.html',{'form':form})
    else:
       form=ContactForm()
    return render(request,'django_form.html',{'form':form})

def StudentForm(request):
    if request.method == "POST":
        form = StudentData(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = StudentData()

    return render(request, 'django_form.html', {'form': form})



def PasswordForm(request):
    if request.method == "POST":
        form = passwordValidationProject(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = passwordValidationProject()

    return render(request, 'django_form.html', {'form': form})