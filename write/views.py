from django.shortcuts import render
from .forms import BoardWriteForm
from .models import Free
from all_info.models import Info

# Create your views here.
def board_list(request):
    login_session = request.session.get('login_session','')
    context = {'login_session' : login_session}
    return render(request, 'wirte/board_list.html', context)

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
                writer=writer
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

    return render(request, 'wirte/board_free_write.html', context)

def free(request):
    free_id = free.objects.all()
    
    return render(
        request,
        'wirte/free.html',
        {'free': free_id}
    )

def join(request):
    join_id = join.objects.all()
    
    return render(
        request,
        'wirte/join.html',
        {'join': join_id}
    )

def gallery(request):
    gallery_id = gallery.objects.all()
    
    return render(
        request,
        'wirte/gallery.html',
        {'gallery': gallery_id}
    )

