from django.shortcuts import render

# Create your views here.
def board_list(request):
    login_session = request.session.get('login_session','')
    context = {'login_session' : login_session}
    return render(request, 'wirte/board_list.html', context)

def board_free_write(request):
    login_session = request.session.get('login_session','')
    context = {'login_session' : login_session}
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

