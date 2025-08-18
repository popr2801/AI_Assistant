from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from django.core.exceptions import ObjectDoesNotExist
from .forms import fileForm, loginForm,registerForm,questionForm
from .utils import handle_file,create_summary
from .models import User,Files

def index(request):
    return render(request,'index.html')

def assistant(request):
    user_id = request.session.get('user_id')
    user = User.objects.get(id=user_id)
    if not user_id:
        return redirect('/index/')
    if request.method == "POST":
        form = questionForm(request.POST)
        if form.is_valid():
            file_text = "There is no file at the moment"
            files = Files.objects.filter(user=user)
            if files.exists():
                file_text = "\n\n".join(f"{f.uploaded_file.name} : {f.file_content}" for f in files)
            answer = create_summary(file_text, form.cleaned_data['question'])
            return HttpResponse(f"<p>{answer}</p>")
    else:
        form = questionForm()
    return render(request,'assistant.html',{'form':form})

def register(request):
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.password_hash = make_password(form.cleaned_data["password"])
            user.save()
            return redirect("/dashboard/")
    else:
        form = registerForm()
    return render(request,'register.html',{'form' : form})

def login(request):
    if request.method == "POST":
        form = loginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            try:
                user = User.objects.get(email=email)
                if check_password(password,user.password_hash):
                    request.session['user_id'] = user.id
                    return redirect('/dashboard/')
                messages.error(request,"Invalid Password")
            except User.DoesNotExist:
                messages.error(request,"User not found")
    else:
        form = loginForm()
    return render(request,'login.html',{'form':form})

def dashboard(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('/login/')
    try:
        user = User.objects.get(id=user_id)
        user_files = user.files.all()
    except ObjectDoesNotExist:
        return redirect('/login/')
    if request.method == "POST":
        form = fileForm(request.POST,request.FILES)
        if form.is_valid():
            file_instance = form.save(commit=False)
            file_instance.file_content = handle_file(file_instance.uploaded_file)
            file_instance.user = user
            file_instance.save()
            return redirect('/dashboard')
    form = fileForm()
    return render(request,'dashboard.html',{'user' : user, 'files' : user_files, 'form' : form})

def delete_file(request,id):
    file = Files.objects.get(id=id)
    file.delete()
    return redirect('/dashboard')
