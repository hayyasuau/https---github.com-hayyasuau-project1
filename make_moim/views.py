from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib import messages
# from django.contrib.auth.mixins import LoginRequiredMixin
from all_info.models import GroupInfo, Info
from make_moim.models import Make_Moim
from write.models import Good


# Create your views here.
def make_moim(request):
    if request.method == 'GET':
        return render(request, 'make_moim/make_moim_form.html')
    name = request.POST.get('name')
    commend = request.POST.get('commend')
    location = request.POST.get('location')
    # imgfile = request.POST.get('imgfile')
    imgfile = request.FILES.get('imgfile')
    max_people = request.POST.get('max_people')
    # make_moims = Make_Moim.objects.all()
    try:
        info_id = request.session['info_id']
        info_id = Info.objects.get(info_id=info_id)
        make_moim = Make_Moim(name=name,commend=commend,location=location,imgfile=imgfile,max_people=max_people)
        make_moim.save()
    except:
        return redirect('/login/')
    # 얘는 다 실행하고 보내는 주소
    return redirect('/board_moim/list')
    # return render(request, 'board_moim/board_list.html',{'name': name,'commend': commend,'location': location,'imgfile': imgfile,'max_people': max_people,'id':make_moim.make_id})

def make_moim_signup(request):
    # 로그인 회원
    info_id = request.session['info_id']
    print(type(info_id))
    info = Info.objects.get(info_id=info_id)
    # 신청 회원
    comment_id=request.GET.get('comment_id', request.POST.get('comment_id'))
    id=Info.objects.get(info_id=comment_id)
    # 가입하려는 모임의 pk
    make_id=request.GET.get('make_id', request.POST.get('make_id'))
    make_moim=Make_Moim.objects.get(pk=make_id)
    #여기서 잠깐 스톱


    if request.method == 'GET':
        context = {
            'make_moim':make_moim,'info':info, 'id':id 
        }

        return render(
            request,
            'make_moim/yes_or_no.html',context
        )

    try :
        selected = request.POST.get('selected')
        if selected == 'Y':
            # Info 와 Make_Moim 연결해서 저장시키기
            # 연결 시킬 것 all_info 아이디랑 Groupinfo->set까지
            # 현재 아이디를 알고 있음 - > 모임의 이름과 연결을 해야함
            now_people = make_moim.now_people
            max_people = make_moim.max_people

            if now_people < max_people:
                make_moim.now_people+=1
                make_moim.save()
                g = GroupInfo()
                g.info = id
                g.make_moim = make_moim
                g.y_n = 'Y'
                g.apply_date = '20230104'
                g.join_date = '????'
                g.save()
                # info = Info.objects.get(info_id='babo')
                # info.info_id = info_id
                # info.save()

            
                context = {
                    'make_moim':make_moim
                }
                return render(request, 'board_moim/detail.html', context)

            else:
                messages.warning(request, '인원이 가득찼습니다.')
                return redirect(f'/board_moim/{make_moim}')

    except :
        return redirect('/login/')
    # return redirect(f'/board_moim/{make_moim}')