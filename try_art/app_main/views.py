from django.shortcuts import render
from django.views.generic.list import ListView
from .models import images_log
# Create your views here.

 # class based views 
 

 
class Imageview(ListView):
    model = images_log
    paginate_by = 4 # number of posts will load
    # context_object_name = "posts"         #?
    template_name = 'home_main.html'
    ordering = ['-title']
    # print(images_log.images_pic)




 # funciton based views 

# def home_main(request):
#     imagesmain = images_log.objects.all()
#     content_main = {'images_p':imagesmain}
#     return render(request,'home_main.html',content_main)

    

def login_main(request):
    print(images_log.title)
    return render(request,'login_main.html')

def register_main(request):
    return render(request,'register_main.html')

def logout_main(request):
    return render(request,'logout_main.html')

def accounts_main(request):
    return render(request,'accounts_main.html')

def enlarger_main(request):
    return render(request,'enlarger_main.html')

# error pages
def handler404(request, exception):
    return render(request, '404.html', status=404)