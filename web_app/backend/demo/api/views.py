from django.shortcuts import render,HttpResponse
from .forms import fileForm, loginForm
from .utils import handle_file,create_summary

def index(request):
    return render(request,'index.html')

def uploadFile(request):
    if request.method == "POST":
        form = fileForm(request.POST,request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES.get('file')
            if uploaded_file == None:
                file_text = "This time theres no file attached"
            else:
                file_text = handle_file(uploaded_file)
            answer = create_summary(file_text,form.cleaned_data['question'])
            return HttpResponse(f"<p>{answer}</p>")
    form = fileForm()
    return render(request,'uploadFile.html',{'form':form})

def login(request):
    form = loginForm(request.POST)
    return render(request,'login.html',{'form':form})