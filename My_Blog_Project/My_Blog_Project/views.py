from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect
def index(request):
    #return HttpResponse("i am home page")
    # this will call the blog list page
    # on the startup
    return HttpResponseRedirect(reverse('App_Blog:blog_list'))
