from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import date
from .models import Author,Tag,Post
from django.views.generic import ListView, DetailView
from .forms import CommentForm
from django.views import View


# Create your views here.

# def starting_page(request):
#      sorted_posts = sorted(all_posts, key=get_date)
#      latest_posts = sorted_posts[-3:]
#      return render(request, "blog/index.html", {"posts": latest_posts}
#      )
def starting_page(request):
  latest_posts = Post.objects.all().order_by("-date")[0:3]
  return render(request, "blog/index.html", {"posts": latest_posts})

class Startingpageview(ListView):
  template_name = "blog/index.html"
  model = Post
  ordering = ["-date"]
  context_object_name = "posts"



  def get_queryset(self):
    queryset =  super().get_queryset()
    data = queryset[:3]
    return data 

    

# def posts(request):
#      return render(request, "blog/all-posts.html", {"posts":all_posts})

def posts(request):
  all_posts = Post.objects.all().order_by("-date")
  return render(request, "blog/all-posts.html", {"posts":all_posts})

class Allpostview(ListView):
  template_name = "blog/all-posts.html" 
  model = Post
  ordering = ["-date"]
  context_object_name = "all_posts"


# def post_detail(request, slug):
#      for post in all_posts:
#        if post["slug"] == slug:
#          identified_post = post
#      return render(request, "blog/post-detail.html", {"post": identified_post})

class SinglePostView(View):
  def get(self,request,slug):
    
    identified_post = Post.objects.get(slug=slug)
    comment_form = CommentForm()
    comments = identified_post.comments.all().order_by("-id")[0:3]
    return render(request, "blog/post_detail.html", {"post": identified_post, "form":comment_form,"comments":comments })
  
  def post(self,request,slug):
    comment_form = CommentForm(request.POST)
    post = Post.objects.get(slug=slug)
    # if comment_form.is_valid():
    #   comment_form.save()
    # Here if we directly save the data taken from the form to database,there can be problem because in the database there is a field called post and in 
    # the form, there was no such field so if i directly save the data to database from form then post will be empty so something needs to be populated for 
    # the post field in the database. 
    comment = comment_form.save(commit=False)
    comment.post = post
    comment.save()
    return HttpResponseRedirect(reverse("post-detail", args=[slug]))

  

#      
# class Singlepostview(DetailView):
#   template_name = "blog/post-detail.html"
#   model = Post
