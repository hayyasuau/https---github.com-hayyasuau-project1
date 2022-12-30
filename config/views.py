from django.shortcuts import redirect, render
from all_info.models import Info

def update(request):
    # GET
    if request.method == 'GET':
        id = request.GET.get('id')
        s = Info.objects.get(pk=id)
        return render(
            request,
            'common/id_pw.html',
            { 'shop': s }
        )
    # POST
    info_id = request.POST.get('info_id')
    pw = request.POST.get('pw')
    name = request.POST.get('name')
    region = request.POST.get('region')
    sex = request.POST.get('sex')
    preference = request.POST.get('preference')
    age = request.POST.get('age')

    s = Info.objects.get(pk=id)
    s.info_id = info_id
    s.pw = pw
    s.name = name
    s.region = region
    s.sex = sex
    s.preference = preference
    s.age = age
    s.save()
    return redirect('/common/loginfo/')