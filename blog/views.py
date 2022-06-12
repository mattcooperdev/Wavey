from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm


class PostList(generic.ListView):
    '''
    View for list of posts on homepage
    paginated by 6 articles each page
    '''
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):
    '''
    View for detailed post page
    with comments on POST view
    '''
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                'comment_form': CommentForm()
            },
            )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
            )


class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class AddPost(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Post
    template_name = "add_post.html"
    fields = ['title', 'featured_image', 'content']
    success_message = "Post created successfully!"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePost(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, generic.UpdateView):
    model = Post
    template_name = "update_post.html"
    fields = ['title', 'featured_image', 'content']
    success_message = "Post updated successfully!"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # function will raise 403 if user tries to update post and is not author
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class DeletePost(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, generic.DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = '/'
    success_message = "Post deleted."

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
