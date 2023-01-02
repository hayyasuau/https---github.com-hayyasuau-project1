from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from all_info.models import Info
from make_moim.models import Make_Moim


# Create your views here.
def make_moim(request):
    if request.method == 'GET':
        return render(request, 'make_moim/make_moim_form.html')
    pk=Make_Moim.objects('make_id')
    name = request.POST.get('name')
    commend = request.POST.get('commend')
    location = request.POST.get('location')
    imgfile = request.POST.get('imgfile')
    max_people = request.POST.get('max_people')
    make_moims = Make_Moim.objects.all()
    make_pk= Make_Moim.objects.get(pk=pk)
    try:
        info_id = request.session['info_id']
        info_id = Info.objects.get(info_id=info_id)
        make_moim = Make_Moim(name=name,commend=commend,location=location,imgfile=imgfile,max_people=max_people)
        make_moim.save()
    except:
        return redirect('/signup/')
    return render(request, 'make_moim/make_moim_form.html',{'name': name,'commend': commend,'location': location,'imgfile': imgfile,'max_people': max_people,'make_moims':make_moims, 'make_pk':make_pk})

def make_detail(request, pk):
    try :
        make_moim= Make_Moim.objects.get(pk=pk)
    except Make_Moim.DoesNotExist:
        raise Http404('해당 게시물을 찾을 수 없습니다.')
    return render(request, 'make_moim/make_detail.html', {'make_moim' : make_moim})
