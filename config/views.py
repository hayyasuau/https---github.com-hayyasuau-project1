from django.shortcuts import redirect, render
from all_info.models import Info

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
    return redirect('loginfo/')