from django.shortcuts import redirect, render
from all_info.models import Info
from file.models import Search
from make_moim.models import Make_Moim
from tag.models import Tag, TagMoim

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
            'common/pages-register.html',
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
            'common/pages-login.html', 
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
    search = request.POST.get('search')
    tag = Tag.objects.filter(name__contains=search)
    make_moim = Make_Moim.objects.filter(name__contains=search)
    category = Make_Moim.objects.filter(category__contains=search)
    context ={
        'search':search, 'make_moim':make_moim, 'tag':tag,
        'category':category
    }
    return render(request, 'search.html', context)
