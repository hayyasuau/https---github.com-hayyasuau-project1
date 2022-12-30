# from django.shortcuts import redirect

# def login_required(func):
#     def wrapper(reuest, *args, **kwargs):
#         login_session = request.session.get('login_session','')
#         if login_session == '':
#             return redirect('login/')
        
#         return func(reuest, *args, **kwargs)
#     return wrapper