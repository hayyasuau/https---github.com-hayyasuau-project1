from django.http import Http404
from django.shortcuts import redirect, render
from django.views.generic import DetailView
from make_moim.models import Make_Moim
from select_moim.models import Select_Moim
from write.models import Good

# Create your views here.
def select_moim(request):
    if request.method == 'POST':
        selects = Select_Moim.objects.all()
        
        return render(
            request,
            'select_moim/select_moim.html',{'select_moims':selects}
        )
    else :
        return render(request, 'select_moim/select_moim.html',{})

# class Select_DetailView(DetailView):

def make_update(request, id):
    make_moim=Make_Moim.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        commend = request.POST.get('commend')
        location = request.POST.get('location')
        imgfile = request.POST.get('imgfile')
        max_people = request.POST.get('max_people')
        
        try : 
            make_moim.name = name
            make_moim.commend = commend
            make_moim.location = location
            make_moim.imgfile = imgfile
            make_moim.max_people = max_people
            make_moim.save()
            return render(request,'make_moim/detail.html')
        except:
            return redirect('/select_moim')

def delete(request, id):
    try :
        make_moim=Make_Moim.objects.get(id=id)
        make_moim.delete()
        return render(request,'make_moim/detail.html')
    except:
        return redirect('/select_moim')

        
def make_detail(request, id):
    try :
        make_moim= Make_Moim.objects.get(id=id)
        good=Good.objects.filter(make_moim=make_moim)

        context = {
            'make_moim' : make_moim,
            'good' : good
            
        }
    except Make_Moim.DoesNotExist:
        raise Http404('해당 게시물을 찾을 수 없습니다.')
    return render(request, 'make_moim/make_detail.html', context)
