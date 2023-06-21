import json
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from accounts.models import Userjob
from decision.models import Decision, Meeting,Recommendation,Rec
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.db.models import Q

class CustomLoginView(LoginView):
    def form_valid(self, form):
        response = super().form_valid(form)

  
     
@login_required(login_url="/login")
def index(request):
    return render(request, "index.html",{"title":'الصفحة الرئيسية'})

@login_required(login_url="/login")
def handler404(request, exception):
    return render(request, '404.html', status=404)

@login_required(login_url="/login")
def meeting(request):

    user = request.user
    jobs = Userjob.objects.filter(user=user)
    all_jobs=[]
    for job in jobs:
        all_jobs.append(job.job_position)
        for i in job.job_position.get_descendants():
            all_jobs.append(i)
    all_jobs = list(set(all_jobs))   
    decision=Decision.objects.filter(Q(responsible=user) | Q(trailing=user))
    m = Meeting.objects.filter(job_position__in=all_jobs,)
    dm=[]
    for d in decision:
        dm.append(d.meettings)
    res=list(m)+dm
    res = list(set(res))   
    return render(request, "meeting.html",context={"meetings":res,"title":'صفحة الجلسات'})

@login_required(login_url="/login")
def recs(request):
    
    r = Recommendation.objects.all().order_by('-id')
    return render(request, "recommendations.html",context={"recs":r,"title":'صفحة التوصيات'})

@login_required(login_url="/login")
def rec(request,pk):
    
    r = Recommendation.objects.get(uuid=pk)
    rec = Rec.objects.filter(recommendation=r)
    return render(request, "recommendation.html",context={"recs":r,"rec":rec,"title":'صفحة التوصية'})

@login_required(login_url="/login")
def meeting_details(request,pk):
    m = Meeting.objects.get(uuid=pk)
    d = Decision.objects.filter(meettings=m)
    return render(request, "meeting_details.html",context={"meeting":m,"decisions":d,"title":'صفحة الجلسة'})


@login_required(login_url="/login")
def decision_details(request,slug,pk):
    m = Meeting.objects.get(uuid=slug)
    d = Decision.objects.get(meettings=m,pk=pk)
    trailing=[]
    responsible=[]
    for i in d.trailing.all():
        trailing.append(i.username)
    for r in d.responsible.all():
        responsible.append(r.username)
    print(trailing)
    return render(request, "decision.html",context={"meeting":m,"decision":d,"trailing":trailing,"responsible":responsible,"title":'صفحة المقرر'})


@login_required(login_url="/login")
def change_done(request,pk):
    if request.method == 'POST':
        jsonData = json.loads(request.body)
        done = jsonData.get('done')
        d= Decision.objects.get(pk=pk)
        d.done=done
        d.save()
        return HttpResponse("OK", status=200)
    
@login_required(login_url="/login")
def account_view(request):
    jobs = Userjob.objects.filter(user=request.user)
    jobs_names=[]
    for job in jobs:
        jobs_names.append(job.job_position.name)
    return render(request, 'account.html', {'user': request.user,"jobs_names":jobs_names,"title":'الصفحة الشخصية'})

@login_required(login_url="/login")
def download_file(request, pk):
    instance = Meeting.objects.get(uuid=pk)
    file_path = instance.metting_file.path
    print(file_path)
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename=' + instance.metting_file.name
        return response

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        valuenext= request.POST.get('next')
        if valuenext is not None:
            full_url = request.build_absolute_uri() + f"?next={valuenext}"
        else:
            full_url="login"
        if user is not None and valuenext is not None:
            login(request, user)
            return redirect(valuenext)
        elif user is not None:
            login(request, user)
            return redirect('home')
        else:
            
            return redirect(full_url)
    return render(request,'login.html',{"title":'صفحة تسجيل الدخول'})