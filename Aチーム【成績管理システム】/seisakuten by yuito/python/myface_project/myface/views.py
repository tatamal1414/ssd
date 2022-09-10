from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.http import request
def top(request):
    
    return render(request, 'top.html')

# class next(TemplateView):
#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)
#         img = request.POST.get("img")
#         context["img"] = img
#         return render(request, 'next.html' , context)


def next(request):
    return render(request, 'next.html')
    # if request.is_ajax():
    #     message = "Yes, AJAX!"
    # else:
    #     message = "Not Ajax"
    # return HttpResponse(message)
