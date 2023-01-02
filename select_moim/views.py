from django.shortcuts import render

from select_moim.models import Select_Moim

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