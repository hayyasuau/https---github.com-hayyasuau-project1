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
    csb=request.POST.get('change_search_bar')
    search = request.POST.get('search')
    
    tag = Tag.objects.filter(name__contains=search).order_by('-pk')
    make_moim = Make_Moim.objects.filter(name__contains=search).order_by('-make_id')
    category = Make_Moim.objects.filter(category__contains=search).order_by('-make_id')

    page = int(request.GET.get('page',1))
    # if not page : page = '1'
    # page=int(page)
    end = page * 5
    start = end - 5
    s_page = (page-1)//10*10 + 1
    e_page = s_page +9

    #페이지 구분 귀찮으니까 각각 페이징 해주자
    tag_count = Tag.objects.filter(name__contains=search).count()
    name_count = Make_Moim.objects.filter(name__contains=search).count()
    category_count = Make_Moim.objects.filter(category__contains=search).count()
    tag_page = tag_count//5 +1
    name_page = name_count//5 +1
    category_page = category_count//5 +1

    if csb == 'all':
        page_tag = int(request.GET.get('page_tag',1)) #태그
        # if not page : page = '1'
        # page=int(page)
        end_tag = page_tag * 5
        start_tag = end_tag - 5
        s_page_tag = (page_tag-1)//10*10 + 1
        e_page_tag = s_page_tag +9
        
        page_ctg = int(request.GET.get('page_ctg',1)) #카테고리
        # if not page : page = '1'
        # page=int(page)
        end_ctg = page_ctg * 5
        start_ctg = end_ctg - 5
        s_page_ctg = (page_ctg-1)//10*10 + 1
        e_page_ctg = s_page_ctg +9
        
        if page_tag > tag_page: #태그
            page_tag = tag_page
            end_tag = page_tag * 5
            start_tag = end_tag -5
        
        if tag_count % 5 !=0:
            tag_page +=1

        if e_page_tag > tag_page : 
            e_page_tag = tag_page
            
        if page > name_page: #모임
            page = name_page
            end = page * 5
            start = end -5
        
        if tag_count % 5 !=0:
            name_page +=1

        if e_page > name_page : 
            e_page = name_page
            
        if page_ctg > category_page: #카테고리
            page_ctg = category_page
            end_ctg = page_ctg * 5
            start_ctg = end_ctg -5
        
        if category_count % 5 !=0:
            category_page +=1

        if e_page_ctg > category_page : 
            e_page_ctg = category_page

        page_info_ctg = range(s_page_ctg, e_page_ctg)
        category_list = category[start:end]
        page_info = range(s_page, e_page)
        moim_list = make_moim[start:end]
        page_info_tag = range(s_page_tag, e_page_tag)
        tag_list = tag[start:end]
        
        context ={
            'search':search, 'make_moim':make_moim, 'tag':tag,
            'category':category,'total_list' : tag_list,
            'page_info' : page_info,
            'page_info_ctg' : page_info_ctg,
            'page_info_tag' : page_info_tag,
            'total_page' : name_page,
            'tag_page' : tag_page,
            'category_page' : category_page,
            'e_page' : e_page,
            'page':page,
            'e_page_tag' : e_page_tag,
            'page_tag':page_tag,
            'e_page_ctg' : e_page_ctg,
            'page_ctg':page_ctg,
        }
        return render(request, 'search.html', context)
    elif csb == 'search_title':
        if page > name_page: #이름
            page = name_page
            end = page * 5
            start = end -5
        
        if name_count % 5 !=0:
            name_page +=1

        if e_page > name_page : 
            e_page = name_page

        page_info = range(s_page, e_page)
        moim_list = make_moim[start:end]
        context ={
            'total_list' : moim_list,
            'page_info' : page_info,
            'total_page' : name_page,
            'e_page' : e_page,
            'page':page,'search':search, 'make_moim':make_moim,
        }
        return render(request, 'search.html', context)
    elif csb == 'tag_title':
        if page > tag_page: #태그
            page = tag_page
            end = page * 5
            start = end -5
        
        if tag_count % 5 !=0:
            tag_page +=1

        if e_page > tag_page : 
            e_page = tag_page

        page_info = range(s_page, e_page)
        tag_list = tag[start:end]
        context ={
            'search':search, 'tag':tag,'total_list' : tag_list,
            'page_info' : page_info,
            'total_page' : tag_page,
            'e_page' : e_page,
            'page':page,
        }
        return render(request, 'search.html', context)
    elif csb == 'category_title':
        if page > category_page: #카테고리
            page = category_page
            end = page * 5
            start = end -5
        
        if category_count % 5 !=0:
            category_page +=1

        if e_page > category_page : 
            e_page = category_page

        page_info = range(s_page, e_page)
        category_list = category[start:end]
        context = {
            'search':search, 'category':category,'total_list' : category_list,
            'page_info' : page_info,
            'total_page' : category_page,
            'e_page' : e_page,
            'page':page,
        }
        return render(request, 'search.html', context)