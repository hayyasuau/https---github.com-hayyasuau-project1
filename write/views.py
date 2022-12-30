from django.shortcuts import render

# Create your views here.
def free(request):
    free_id = free.objects.all()
    
    return render(
        request,
        'wirte/free.html',
        { 'free': free_id}
    )