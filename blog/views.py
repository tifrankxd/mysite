from pyexpat.errors import messages
from urllib import request
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.shortcuts import get_object_or_404
from django.views import generic
from django.contrib.messages import add_message
from django.contrib import messages

from .forms import CommentForm
from .models import Post, Ad, SocialLink


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 3


# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'


def post_detail(request, slug):
    post = Post.objects.filter(slug=slug).first()

    if post is None:
        raise Http404("Post not found")

    return render(request, "blog/post_detail.html", {"post": post})


def post_detail(request, slug):
    template_name = "post_detail.html"
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True).order_by("-created_on")
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    ads = Ad.objects.all()

    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
            "ads": ads,
        },
    )


def nosotros(request):
    social_links = SocialLink.objects.all()
    return render(request, "nosotros.html", {"social_links": social_links})


def about(request):
    # Check if the session variable 'cookie_message_shown' exists
    if not request.session.get("cookie_message_shown", False):
        # Display the cookie message only once per session
        messages.info(
            request,
            "Este sitio utiliza cookies. Al continuar navegando, aceptas su uso.",
        )

        # Set the session variable to prevent further messages
        request.session["cookie_message_shown"] = True

    return render(request, "about.html")


def policy(request):
    ads = Ad.objects.all()
    return render(request, "policy.html")
