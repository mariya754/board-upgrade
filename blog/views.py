from django.views.generic import ListView, DetailView# новое 
from django.shortcuts import render, get_object_or_404
from django import forms
from django.forms import inlineformset_factory
from django.contrib import messages
from django.shortcuts import redirect

from .models import Post, AdditionalImage, Comment
from .forms import  PostForm, AIFormSet, CommentForm
 
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
    initial = {'bb': bb.pk}
    form_class = CommentForm
    form = form_class(initial=initial)

    if request.method == 'POST':
        comment_form = form_class(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            messages.add_message(request, messages.SUCCESS, 'Комментарий добавлен')
        else:
            form = comment_form
            messages.add_message(request, messages.WARNING, 'Комментарий недобавлен')

    context = {'bb':bb, 'ais':ais, 'comments': comments, 'form': form}
    return render(request, 'post_detail.html', context) 

# def detail(request, rubric_pk, pk):
#     bb = get_object_or_404(Bb, pk=pk)
#     ais = bb.additionalimage_set.all()
#     comments = Comment.objects.filter(bb = pk, is_active=True)
#     initial = {'bb': bb.pk}
#     if request.user.is_authenticated:
#         initial['author'] = request.user.username
#         form_class = UserCommentForm
#     else:
#         form_class = GuestCommentForm
#     form = form_class(initial=initial)
#     if request.method == 'POST':
#         comment_form = form_class(request.POST)
#         if comment_form.is_valid():
#             comment_form.save()
#             messages.add_message(request, messages.SUCCESS, 'Комментарий добавлен')
#         else:
#             form = comment_form
#             messages.add_message(request, messages.WARNING, 'Комментарий недобавлен')

    context = {'bb':bb, 'ais':ais, 'comments': comments, 'form': form}
    return render(request, 'main/detail.html', context) 

#     bbs = Bb.objects.filter(author=request.user.pk)
#     context = {'bbs': bbs}
#     return render(request, 'main/profile.html', context)

# class BBLogoutView(LoginRequiredMixin, LogoutView):
#     template_name = 'main/logout.html'


# class BBLoginView(LoginView):
#     template_name = 'main/login.html'


# class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
#     model = AdvUser
#     template_name = 'main/change_user_info.html'
#     form_class = ChangeUserInfoForm
#     success_url = reverse_lazy('main:profile')
#     success_message = 'Данный пользователя успешно изменены!'

#     def setup(self, request, *args, **kwargs):
#         self.user_id = request.user.pk
#         return super().setup(request, *args, **kwargs)

#     def get_object(self, queryset = None):
#         if not queryset:
#             queryset = self.get_queryset()
#         return get_object_or_404(queryset, pk = self.user_id)


# class BBPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
#     template_name = 'main/password_change.html'
#     success_url = reverse_lazy('main:profile')
#     success_message = 'Пароль пользователя успешно изменен'

# class RegisterUserView(CreateView):
#     model = AdvUser
#     template_name = 'main/register_user.html'
#     form_class = RegisterUserForm
#     success_url = reverse_lazy('main:register_done')


# class RegisterDoneView(TemplateView):
#     template_name = 'main/register_done.html'

# def user_activate(request, sign):
#     try:
#         username = signer.unsign(sign)
#     except BadSignature:
#         return render(request, 'main/bad_signature.html')
#     user = get_object_or_404(AdvUser, username = username)
#     if user.is_activated:
#         template = 'main/user_is_activated.html'
#     else:
#         template = 'main/activation_done.html'
#         user.is_active = True
#         user.is_activated = True
#         user.save()
#     return render(request, template)


# class DeleteUserView(LoginRequiredMixin, DeleteView):
#     model = AdvUser
#     template_name = 'main/delete_user.html'
#     success_url = reverse_lazy('main:index')

#     def setup(self, request, *args, **kwargs):
#         self.user_id = request.user.pk
#         return super().setup(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         logout(request)
#         messages.add_message(request, messages.SUCCESS, 'Пользователь удален!')
#         return super().post(request, *args, **kwargs)

#     def get_object(self, queryset = None):
#         if not queryset:
#             queryset = self.get_queryset()

#         return get_object_or_404(queryset, pk = self.user_id)

# def by_rubric(request, pk):
#     rubric = get_object_or_404(SubRubric, pk = pk)
#     bbs = Bb.objects.filter(is_active = True, rubric = pk)
#     if 'keyword' in request.GET:
#         keyword = request.GET['keyword']
#         q = Q(title__icontains = keyword) | Q(content__icontains = keyword)
#         bbs = bbs.filter(q)
#     else:
#         keyword = ''
#     form = SearchForm(initial={'keyword': keyword})
#     paginator = Paginator(bbs, 2)
#     if 'page' in request.GET:
#         page_num = request.GET['page']
#     else:
#         page_num = 1
#     page = paginator.get_page(page_num)
#     context = {'rubric': rubric, 'page': page, 'bbs': page.object_list, 'form': form}
#     return render(request, 'main/by_rubric.html', context)



# @login_required
# def profile_add(request):
#     if request.method == 'POST':
#         form = BbForm(request.POST, request.FILES)
#         if form.is_valid():
#             bb = form.save()
#             formset = AIFormSet(request.POST, request.FILES, instance=bb)
#             if formset.is_valid():
#                 formset.save()
#                 messages.add_message(request, messages.SUCCESS, 'Объявление добавлено')

#     else:
#         form = BbForm(initial={'author':request.user.pk})
#         formset = AIFormSet()
#     context = {'form':form, 'formset':formset}
#     return render(request, 'main/profile_bb_add.html', context)


def change(request, pk):
   bb = get_object_or_404(Post, pk=pk)
   if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=bb)
        if form.is_valid():
             bb = form.save()
             formset = AIFormSet(request.POST, request.FILES, instance=bb)
             if formset.is_valid():
                 formset.save()
                 messages.add_message(request, messages.SUCCESS, 'Объявление изменено')
        return redirect('home')
   else:
        form = PostForm(instance=bb)
        formset = AIFormSet(instance=bb)
   context = {'form':form, 'formset':formset}
   return render(request, 'post_change.html', context)


def delete(request, pk):
    bb = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        bb.delete()
        messages.add_message(request, messages.SUCCESS, 'Объявление удалено')
        return redirect('home')
    else:
        context = {'bb': bb}
        return render(request, 'post_delete.html', context)