from django.views.generic import ListView, DetailView# новое 
from django.shortcuts import render, get_object_or_404
from django import forms
from django.forms import inlineformset_factory

from .models import Post, AdditionalImage, Comment
 
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
 
 
class BlogDetailView(DetailView): # новое
    model = Post 
    template_name = 'post_detail.html'

  #  class Meta:
   #     model = Post
     #   fields = '__all__'

#AIFormSet = inlineformset_factory(Post, AdditionalImage, fields = '__all__')

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {'author': forms.HiddenInput}

AIFormSet = inlineformset_factory(Post, AdditionalImage, fields = '__all__')      


class UserCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ('is_active',)
        widgets = {'bb': forms.HiddenInput}


def detail(request, pk):
    bb = get_object_or_404(Post, pk=pk)
    ais = bb.additionalimage_set.all()
    comments = Comment.objects.filter(bb = pk)
    # initial = {'bb': bb.pk}
    # form_class = UserCommentForm

    # if request.method == 'POST':
    #     comment_form = form_class(request.POST)
    #     if comment_form.is_valid():
    #         comment_form.save()
    #         messages.add_message(request, messages.SUCCESS, 'Комментарий добавлен')
    #     else:
    #         form = comment_form
    #         messages.add_message(request, messages.WARNING, 'Комментарий недобавлен')

    context = {'bb':bb, 'ais':ais, 'comments': comments, }
    return render(request, 'post_detail.html', context) 


