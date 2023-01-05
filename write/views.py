from django.urls import reverse
from django.shortcuts import  get_object_or_404,render, redirect

from make_moim.models import Make_Moim
from .forms import BoardWriteForm, GoodForm
from .models import Free, Gallery, Join ,Good
from all_info.models import Info
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
# from django.view.decorators.http import require_http_methods

# def test(request):
#     board_list = Free.objects.all() #models.py Free 클래스의 모든 객체를 board_list에 담음
#     # board_list 페이징 처리
#     page = request.GET.get('page', '1') #GET 방식으로 정보를 받아오는 데이터
#     paginator = Paginator(board_list, '5') #Paginator(분할될 객체, 페이지 당 담길 객체수)
#     page_obj = paginator.page(page) #페이지 번호를 받아 해당 페이지를 리턴 get_page 권장
#     return render(request, 'template_name', {'page_obj':page_obj}) 


def text_delete(request,free_id, pk):#글삭
    login_session = request.session.get('info_id','')
    
    board = get_object_or_404(Free, free_id=pk)
    make_moim = Make_Moim.objects.get(make_id=free_id)

    if board.info.info_id == login_session:
        board.delete()
        return redirect('write:free', free_id)
    else:
        return redirect('write:free', free_id)

def text_modify(request,free_id, pk):#수정
    login_session = request.session.get('info_id','')
    make_moim = Make_Moim.objects.get(make_id=free_id)

    context = {'login_session' : login_session}

    board = get_object_or_404(Free, free_id=pk)
    context['board'] = board
    context['make_moim'] = make_moim

    if request.method == 'GET' :
        return render(request, 'write/modify.html', context)
    
    elif request.method =='POST':
        title = request.POST.get('title')
        text = request.POST.get('text')

        board.title=title
        board.text=text

        board.save()
        return redirect('write:free', free_id)


def view_text(request,free_id,pk): #게시물 보기
    free=Free.objects.get(free_id=pk)
    make_moim = Make_Moim.objects.get(make_id=free_id)
    return render(request, 'write/vt_free.html',{'free':free,'make_moim':make_moim })

def freeboard_index(request, free_id): #자유게인덱스
    all_boards = Free.objects.all().order_by("-write_dttm") # 모든 데이터 조회, 내림차순(-표시) 조회
    make_moim=Make_Moim.objects.get(make_moim=free_id)
    print(make_moim)
    print(free_id)
    return render(request, 'write/freeindex.html', {'title':'Board List', 'board_list':all_boards})

def board_list(request):
    login_session = request.session.get('login_session','')
    context = {'login_session' : login_session}
    return render(request, 'base.html', context)

def board_free_write(request, free_id):#작성 
    login_session = request.session.get('info_id','')
    context = {'login_session' : login_session}

    make_moim = Make_Moim.objects.get(make_id=free_id)
    free=Free.objects.filter(make_moim=make_moim) #어떤 모임에서 써진 글들

    if request.method == 'GET' :
        write_form = BoardWriteForm
        context['forms'] = write_form
        context['make_moim']=make_moim
        return render(request, 'write/board_free_write.html', context)
    elif request.method =='POST':
        write_form = BoardWriteForm(request.POST, request.FILES)

        if write_form.is_valid():
            writer = Info.objects.get(info_id=login_session)
            board = Free(
                title=write_form.title,
                text=write_form.text,
                info=writer,
                imgfile=write_form.imgfile
                # comment=write_form.info
            )
            board.save()
            return redirect('write:free',free_id=free_id)
        
        else:
            context['forms'] = write_form
            context['make_moim']=make_moim
            if write_form.errors:
                for value in write_form.errors.values():
                    context['error'] = value
            return render(request, 'write/board_free_write.html',context)

    return render(request, 'write/board_free_write.html', context)

def free(request, free_id):
    make_moim=Make_Moim.objects.get(make_id=free_id)
    free_id = Free.objects.all().order_by('-pk')
    all_boards = Free.objects.all().order_by("-write_dttm")
    context = {
        'free': free_id, 'board_list':all_boards, 'make_moim':make_moim
    }
    return render(
        request,
        'write/free.html',
        context
    )

def join(request):
    join_id = Join.objects.all().order_by('-pk')
    
    return render(
        request,
        'write/join.html',
        {'join': join_id}
    )

def new_face(request):
    new_face_id = Join.objects.all().order_by('-pk')
    
    return render(
        request,
        'write/new_face.html',
        {'new_face': new_face_id}
    )
def gallery(request):
    gallery_list = Gallery.objects.all().order_by('-pk')
    
    return render(
        request,
        'write/gallery.html',
        {'gallery_list': gallery_list}
    )

def gallery_makeit(request):
    return render(request, 'write/gallery_makeit.html')

def gallery_make(request):
    gallery = Gallery.objects.all().order_by('-pk')

    if request.method == 'POST':
        #회원정보 조회
        files = request.POST.get('files')
        text = request.POST.get('text')
        title = request.POST.get('title')
        
        try:
            info = request.session['info']
            info_id=Info.objects.get(info_id=info)
            new_gallery = Gallery()
            new_gallery.comment =text
            new_gallery.title = title
            new_gallery.imgfile = files
            new_gallery.save()
            return HttpResponseRedirect('write:gallery')
        except:
            return render(request, 'login_fail.html')
    return render(request, 'gallery_makeit.html')

def gallery_single(request, pk, ga): #FBV로 싱글갤러리 만들기
    gallery_singles = Gallery.objects.get(pk=pk)

    return render(request, 'write/single_gallery.html', {'single_gallery':gallery_singles})

# def GalleryCreate(CreateView):
#     model = Gallery
#     field = ['title', 'comment','imgfile','info']

def gallery_free_write(request):
    login_session = request.session.get('login_session','')
    context = {'login_session' : login_session}
    if request.method == 'GET' :
        write_form = BoardWriteForm
        context['forms'] = write_form
        return render(request, 'write/gallery_free_write.html', context)
    
    elif request.method =='POST':
        write_form = BoardWriteForm(request.POST)

        if write_form.is_valid():
            writer = Info.objects.get(user_id=login_session)
            board = Free(
                title=write_form.title,
                texts=write_form.text,
                writer=writer,
                board_name=write_form.info
            )
            board.save()
            return redirect('/gallery_write')
        
        else:
            context['forms'] = write_form
            if write_form.errors:
                for value in write_form.errors.values():
                    context['error'] = value
            return render(request, 'write/gallery_free_write.html',context)

    return render(request, 'write/gallery_free_write.html', context)

def product_create(request):
    if request.method == 'POST':
        form = BoardWriteForm(request.POST, request.FILES) # 꼭 !!!! files는 따로 request의 FILES로 속성을 지정해줘야 함
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.detailfunc = product.detailfunc.replace("'", "").replace("[", "").replace("]", "")
            product.save()
            return redirect('sales:index')
    else:
        form = BoardWriteForm() # request.method 가 'GET'인 경우
    context = {'form':form}
    return render(request, 'sales/product_form.html', context)

# @require_POST
def comments_create(request, pk, gg):
    if request.user.is_authenticated:
        free_text = get_object_or_404(Free, pk=pk)
        comment_form = GoodForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.free = free_text
            comment.free_id = request.free_id
            comment.save()
        return redirect('write:detail', free.pk)
    return redirect('accounts:login')


# @require_POST
def comments_delete(request, join_pk, comment_pk):
    if request.free_id.is_authenticated:
        comment = get_object_or_404(Good, pk=comment_pk)
        if request.free_id == comment.free_id:
            comment.delete()
    return redirect('write:detail', join_pk)

# @require_POST
def likes(request, join_pk):
    if request.free_id.is_authenticated:
        join = get_object_or_404(Free, pk=join_pk)

        if join.like_users.filter(pk=request.free_id.pk).exists():
            join.like_users.remove(request.free_id)
        else:
            join.like_users.add(request.free_id)
        return redirect('join:index')
    return redirect('accouts:login')


def get_absolute_url(self):        
    return f'/write/gallery/{self.pk}/'

#join
def join_detail(request, make_id):
    make_moim=Make_Moim.objects.get(make_id=make_id)
    page = int(request.GET.get('page',1))
    # if not page : page = '1'
    # page=int(page)
    join_lists = Join.objects.all().order_by('-write_dttm')
    end = page * 20
    start = end - 20
    s_page = (page-1)//10*10 + 1
    e_page = s_page +9
    #페이지 구분
    total_count = Join.objects.all().count()
    total_page = total_count//20 +1
    # if page > total_page:
    #     page = total_page
    #     end = page * 5
    #     start = end -5
    
    # if total_count % 10 !=0:
    #     total_page +=1

    if e_page > total_page : 
        e_page = total_page
        
    page_info = range(s_page, e_page+1)
    join_lists = join_lists[start:end]


    # join = Join.objects.get(join_id)
    # comments = Good.objects.filter(good_id=join)   
    context = {
        'join_lists' : join_lists,
        'page_info' : page_info,
        'total_page' : total_page,
        'e_page' : e_page,
        'page':page,
        'make_moim':make_moim
        # 'comments':comments
    }
    

    return render(request, 'write/join_detail.html',context)


def join_comment(request, make_id):
    if request.method == 'GET':
        comment = request.GET.get('comment')
        # join_id = request.GET.get('join_id')
        # join은 아직 안받음??// 모임아이디 ->join을 찾아야 하기 때문에 join 이외에서 불러와야함
        # 여기서는 make_moim에서 가져오자
        make_moim=request.GET.get('make_moim')
        writer = request.GET.get('writer')
        title = request.GET.get('title')
        #아래에서 모임을 조회
        joins = Join.objects.get(make_moim=make_moim)
        # c = Good(content=comment, join=join_id)
        # c.save 댓글을 만들때 처리
        context = {
        'writer':writer,
        'title':title,
        'joins':joins,
        'comment':comment,
        }
        return render(request, 'write/join_detail.html',context)