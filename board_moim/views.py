from django.shortcuts import redirect, render
from all_info.models import GroupInfo, Info
# from django.core.paginator import Paginator
from make_moim.models import Make_Moim
from tag.models import Tag, TagMoim
from write.models import Good
# from django.contrib import messages

# Create your views here.
def board_moim(request):
    return render(request,'board_moim/board.html')
    
def list_moim(request):
    page = int(request.GET.get('page',1))
    # if not page : page = '1'
    # page=int(page)
    moim_lists = Make_Moim.objects.all().order_by('-make_id')
    end = page * 5
    start = end - 5
    s_page = (page-1)//10*10 + 1
    e_page = s_page +9

    #페이지 구분
    total_count = Make_Moim.objects.all().count()
    total_page = total_count//5 +1
    print(total_page)
    # if page > total_page:
    #     page = total_page
    #     end = page * 5
    #     start = end -5
    
    # if total_count % 10 !=0:
    #     total_page +=1

    if e_page > total_page : 
        e_page = total_page

    page_info = range(s_page, e_page+1)
    moim_lists = moim_lists[start:end]

    context = {
        'moim_lists' : moim_lists,
        'page_info' : page_info,
        'total_page' : total_page,
        'e_page' : e_page,
        'page':page
        # 'posts' : posts
    }
    return render(request,'board_moim/board_list.html', context)

def board_detail(request, pk):
    make_moim = Make_Moim.objects.get(make_id=pk)
    groupinfo = GroupInfo.objects.filter(make_moim=make_moim)
    comments = Good.objects.filter(make_moim=make_moim)
    context ={
        'make_moim':make_moim, 'comments':comments, 'groupinfo':groupinfo
    }
    return render(request, 'board_moim/detail.html',context)

def board_update(request, pk):
    make_moim = Make_Moim.objects.get(make_id=pk)
    if request.method == 'POST':
        make_id = request.POST.get('make_id')
        name = request.POST.get('name')
        commend = request.POST.get('commend')
        imgfile = request.POST.get('imgfile')
        location = request.POST.get('location')
        max_people = request.POST.get('max_people')
        category = request.POST.get('category')
        alltag=request.POST.get('tag')
        tags = alltag.split(',')
        
        try :
            TagMoim.objects.filter(make_moim=make_moim).delete()
            for i in tags:
                newtag = Tag(name=i)
                newtag.save()
                tag_id=Tag.objects.all().order_by('-pk')[0]
                t = TagMoim()
                         
                make_moim.make_id = make_id
                make_moim.name = name
                make_moim.commend = commend
                make_moim.imgfile = imgfile
                make_moim.location = location
                make_moim.max_people = max_people
                make_moim.category = category
            # make_moim.tags = tags
                make_moim.save()
                
                t.tag = tag_id   
                t.make_moim = make_moim
                t.save()

            # return render(request, 'board_moim/detail.html')
            return redirect(f'/board_moim/{pk}/')
        except Exception as e:
            print(e)
            return render(request, 'board_moim/update_fail.html',{'make_moim':make_moim})

    return render(request, 'board_moim/update.html',{'make_moim':make_moim})

def board_delete(request, pk):
    make_moim = Make_Moim.objects.get(make_id=pk)
    make_moim.delete()
    return redirect('/board_moim/list/')

def comment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        id = request.POST.get('id')
        make_moim = Make_Moim.objects.get(make_id=id)
        info_id=request.session.get('info_id')
        info=Info.objects.get(info_id=info_id)
        c = Good(content=comment, make_moim=make_moim, info=info)
        c.save()
        return redirect('/board_moim/%s/' %  id)

    # return render(request, 'board_moim/detail.html',{'make_moim':make_moim})

# def search(request, search):
#     search_keyword = request.GET.get('q','')
#     search_type = request.GET.get('type','')
#     moim_lists = Make_Moim.objects.all().order_by('-make_id')
#     if search_keyword:
#         if len(search_keyword) > 1 :
#             if search_type == 'all':
#                 pass
#         else :
#             messages.error(self.request, '검색어는 2글자 이상 입력하세요')
            