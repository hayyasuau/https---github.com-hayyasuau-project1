from django.urls import reverse
from django.shortcuts import HttpResponseRedirect, get_object_or_404,render, redirect
from .forms import BoardWriteForm, GoodForm
from .models import Free, Gallery, Join ,Good
from all_info.models import Info

# Create your views here.
def board_list(request):
    login_session = request.session.get('login_session','')
    context = {'login_session' : login_session}
    return render(request, 'write/board_list.html', context)

# def board_left(request):
#     return render(request, 'write/board_left.html')

def board_free_write(request):
    login_session = request.session.get('login_session','')
    context = {'login_session' : login_session}
    if request.method == 'GET' :
        write_form = BoardWriteForm
        context['forms'] = write_form
        return render(request, 'write/board_free_write.html', context)
    
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
            return redirect('/free_write')
        
        else:
            context['forms'] = write_form
            if write_form.errors:
                for value in write_form.errors.values():
                    context['error'] = value
            return render(request, 'write/board_free_write.html',context)

    return render(request, 'write/board_free_write.html', context)

def free(request):
    free_id = Free.objects.all().order_by('-pk')
    
    return render(
        request,
        'write/free.html',
        {'free': free_id}
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
def gallery_single(request, pk): #FBV로 싱글갤러리 만들기
    gallery_singles = Gallery.objects.get(pk=pk)

    return render(request, 'write/single_gallery.html', {'single_gallery':gallery_singles})


def gallery_make(request):
    gallery = Gallery.objects.all().order_by('-pk')
    
    if request.method == 'POST':
        files = request.POST.get('files')
        text = request.POST.get('text')
        new_gallery = Gallery()
        new_gallery.comment =text
        new_gallery.imgfile = files
        new_gallery.save()
        return HttpResponseRedirect(reverse('write:gallery'))
    else :
        new_gallery_list=new_gallery.objects.all()
        return render(
            request,
            # 이거 아래꺼 list로 하면 list로 보내지나?
            'write/gallery_list.html',
            {'gallery_list': new_gallery_list}
        )
        

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
def comments_create(request, pk):
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
def comments_delete(request, article_pk, comment_pk):
    if request.free_id.is_authenticated:
        comment = get_object_or_404(Good, pk=comment_pk)
        if request.free_id == comment.free_id:
            comment.delete()
    return redirect('write:detail', article_pk)

# @require_POST
def likes(request, article_pk):
    if request.free_id.is_authenticated:
        article = get_object_or_404(Free, pk=article_pk)

        if article.like_users.filter(pk=request.free_id.pk).exists():
            article.like_users.remove(request.free_id)
        else:
            article.like_users.add(request.free_id)
        return redirect('articles:index')
    return redirect('accouts:login')


# def get_absolute_url(self):        
#     return reverse('write:garellry_detail', kwargs={'pk':self.id} )