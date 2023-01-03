from django.shortcuts import render
from django.core.paginator import Paginator
from make_moim.models import Make_Moim

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
