from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from all_info.models import Info
from make_moim.models import Make_Moim
from write.models import Good


# Create your views here.
def make_moim(request):
    if request.method == 'GET':
        return render(request, 'make_moim/make_moim_form.html')
    name = request.POST.get('name')
    print(name)
    commend = request.POST.get('commend')
    location = request.POST.get('location')
    imgfile = request.POST.get('imgfile')
    max_people = request.POST.get('max_people')
    print(max_people)
    make_moims = Make_Moim.objects.all()
    try:
        print('aaaa')
        info_id = request.session['info_id']
        info_id = Info.objects.get(info_id=info_id)
        make_moim = Make_Moim(name=name,commend=commend,location=location,imgfile=imgfile,max_people=max_people)
        make_moim.save()
    except:
        print('bbbb')
        return redirect('/signup/')
    print('cccc')
    # 얘는 다 실행하고 보내는 주소
    return render(request, 'make_moim/make_moim_form.html',{'name': name,'commend': commend,'location': location,'imgfile': imgfile,'max_people': max_people,'make_moims':make_moims,'id':make_moim.make_id})

