from django.shortcuts import redirect, render
from all_info.models import Info
from file.models import Search

def update(request):
    # GET
    if request.method == 'GET':
    
        return render(
            request,
            'common/id_pw.html',
        )
    # POST
    info_id = request.POST.get('info_id')
    pw = request.POST.get('pw')
    name = request.POST.get('name')
    region = request.POST.get('region')
    sex = request.POST.get('sex')
    preference = request.POST.get('preference')
    age = request.POST.get('age')

    s = Info()
    s.info_id = info_id
    s.pw = pw
    s.name = name
    s.region = region
    s.sex = sex
    s.preference = preference
    s.age = age
    s.save()
    #회원가입 코드
    return redirect('loginfo/')#다른 주소로 보낼것

def signup(request):
    # GET
    if request.method == 'GET':
    
        return render(
            request,
            'common/id_pw.html',
        )
    # POST
    info_id = request.POST.get('info_id')
    pw = request.POST.get('pw')
    name = request.POST.get('name')
    region = request.POST.get('region')
    sex = request.POST.get('sex')
    preference = request.POST.get('preference')
    age = request.POST.get('age')

    s = Info()
    s.info_id = info_id
    s.pw = pw
    s.name = name
    s.region = region
    s.sex = sex
    s.preference = preference
    s.age = age
    s.save()
    #회원가입 코드
    return redirect('home')# 다른사이트로 보낼거임

def login(request): #로그인
    # GET
    if request.method == 'GET':
    
        return render(
            request,
            'common/login.html', 
        )
    # POST
    info_id = request.POST.get('info_id')
    pw = request.POST.get('pw')

    try:
        s = Info.objects.get(pk=info_id, pw=pw)
    except:
        return redirect('login')

    request.session['info_id'] = s.info_id
    
    return redirect('home')# 다른사이트로 보낼거임

def logout(request):
    del request.session['info_id']
    return redirect('home')

def home(request):
    return render(request, 'home.html')

from write.models import Free
def search(request):
    search = request.GET.get('search')
    searchs = Free.objects.filter(title__contains=search)
    return render(request, 'search.html', {'search':search,'searchs':searchs})
