from django.shortcuts import render
from django.views import View
from .forms import *
from .models import *

# Create your views here.
def startpage(request):
    return render(request,"mentapp/home.html")

#ADDING NEW POST
def new_post(request):
    post_form=NewPostForm()
    if request.method=="POST":
        post_form= NewPostForm(request.POST)
        # if post_form.is_valid():
        post_form.save()
    context={
        "new_post_form":post_form
    }
    return render(request, 'mentapp/newpost.html',context)






# class NewPostView(View):

#     def get(self, request):
#         context={"new_post_form":NewPostForm()}
#         return render(request,"mentapp/newpost.html", context)

#     def post(self, request):
#         new_post_form=NewPostForm(request.POST)
#         if new_post_form.is_valid():
#             new_post_form.save()
#         context={
#             "new_post_form":new_post_form
#         }
#         return render(request, "mentapp/newpost.html",context )

        # new_post_form=NewPostForm(request.POST)
        # print(request.POST)
        # all_post=NewPost.objects.all()

        # if new_post_form.is_valid():
        #     new_post=new_post_form.save()
        #     new_post.all_post=all_post
        #     return render(request, "mentapp/newpost.html" )