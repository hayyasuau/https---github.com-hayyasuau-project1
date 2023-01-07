from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib import messages
# from django.contrib.auth.mixins import LoginRequiredMixin
from all_info.models import GroupInfo, Info
from make_moim.models import Make_Moim
from tag.models import Tag


# Create your views here.
def make_moim(request):
    info_id = request.session['info_id']
    moim_chief = request.POST.get('moim_chief')
    if request.method == 'GET':
        return render(request, 'make_moim/make_moim_form.html')
    
    if info_id == moim_chief:
        name = request.POST.get('name')
        commend = request.POST.get('commend')
        location = request.POST.get('location')
        # imgfile = request.POST.get('imgfile')
        imgfile = request.FILES.get('imgfile')
        max_people = request.POST.get('max_people')
        category = request.POST.get('category')
        # make_moims = Make_Moim.objects.all()
        try:
            make_moim = Make_Moim(name=name, commend=commend, location=location, imgfile=imgfile, max_people=max_people, category=category )
            make_moim.save()
        except:
            return HttpResponse('<h1>저장에 실패하였습니다.</h1><br><a herf="make_moim:make_moim">뒤로가기</a>')
    else :
        return redirect('/login/')
    # 얘는 다 실행하고 보내는 주소
    return redirect('/board_moim/list')
    # return render(request, 'board_moim/board_list.html',{'name': name,'commend': commend,'location': location,'imgfile': imgfile,'max_people': max_people,'id':make_moim.make_id})


def make_moim_signup(request):
    # 로그인 회원
    info_id = request.session['info_id']
    # print(type(info_id))
    info = Info.objects.get(info_id=info_id)
    # 신청 회원
    comment_id = request.GET.get('comment_id', request.POST.get('comment_id'))
    id = Info.objects.get(info_id=comment_id)
    # 가입하려는 모임의 pk
    make_id = request.GET.get('make_id', request.POST.get('make_id'))
    # print('makeid %s' % make_id)
    make_moim = Make_Moim.objects.get(pk=make_id)
    groupmoim = GroupInfo.objects.filter(make_moim=make_moim)
    #여기서 잠깐 스톱
    # print(list(groupmoim))
    # newmoim=[]
    # for i in list(groupmoim):
    #     print(i.info_id)

    # ininfo=Info.objects.get(info_id=groupmoim)

    if request.method == 'GET':
        context = {
            'make_moim': make_moim, 'info': info, 'id': id
        }

        return render(
            request,
            'make_moim/yes_or_no.html', context
        )


    selected = request.POST.get('selected')
    if selected == 'Y':
        max_people = make_moim.max_people
        try:
            GroupInfo.objects.get(info=id, make_moim=make_moim)
            messages.warning(request, '현재 등록된 인원입니다.')
            print('현재 등록된 인원입니다.')
            return redirect(f'/board_moim/{make_moim.make_id}/')
        except:
            if groupmoim.count() < max_people:
                # Info 와 Make_Moim 연결해서 저장시키기
                # 연결 시킬 것 all_info 아이디랑 Groupinfo->set까지
                # 현재 아이디를 알고 있음 - > 모임의 이름과 연결을 해야함
                # now_people = make_moim.now_people
                g = GroupInfo()
                g.info = id
                g.make_moim = make_moim
                # g.y_n = 'Y'
                # g.apply_date = '20230104'
                # g.join_date = '????'

                # g += g
                g.save()
                # info = Info.objects.get(info_id='babo')
                # info.info_id = info_id
                # info.save()

                # context = {
                #     'make_moim':make_moim
                # }
                return redirect(f'/board_moim/{make_moim.make_id}/')

            else:
                messages.warning(request, '인원이 가득찼습니다.')
                print('인원이 가득찼습니다.')
                return redirect(f'/board_moim/{make_moim.make_id}/')


    # return redirect(f'/board_moim/{make_moim}')
    

