from django.shortcuts import redirect, render

from all_info.models import Info

# Create your views here.
def profile_view(request):
    # if request.method == 'get':

        return render(request, 'all_info/profile.html')
    # else :
    #     return redirect('/login/')
def detail(request, id):
    user = Info.objects.get(info_id=id)
    return render(request, 'all_info/detail.html', {'user' : user})
def update(request, id):
    user = Info.objects.get(info_id=id)
    if user.info_id == request.session['info_id']:

        if request.method == 'POST':
            info_id = request.POST.get('info_id')
            name = request.POST.get('name')
            region = request.POST.get('region')
            sex = request.POST.get('sex')
            preference = request.POST.get('preference')
            age = request.POST.get('age')
            user = Info.objects.get(info_id=id)

            try :
                user.info_id = info_id
                user.name = name
                user.region = region
                user.sex = sex
                user.preference = preference
                user.age = age
                user.save()
                return render(request, 'all_info/detail.html', {'user':user}) #유저친화적
            except :
                return render(request, 'update_fail.html')
    else :
        return redirect('login')
    #받아올 것 먼저 만들기
    return render(request,'all_info/update.html',{'user':user})

