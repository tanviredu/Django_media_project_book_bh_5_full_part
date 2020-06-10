from django.shortcuts import render

def blog_list(request):
    c={}
    return render(request,'App_Blog/blog_list.html',c)
