from django.shortcuts import render
from django.views.generic import TemplateView, FormView, DetailView
from .forms import FormsView
from .models import Post
from django.contrib import messages

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['post'] = Post.objects.all().order_by('-id')
        return context

class DetailPageView(DetailView):
    template_name = 'details.html'
    model = Post

class FormPageView(FormView):
    template_name = 'form.html'
    form_class = FormsView
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super(FormPageView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        create_obj = Post.objects.create(
            text=form.cleaned_data['text'],
            image=form.cleaned_data['image']
        )
        messages.add_message(self.request, messages.SUCCESS, 'Uploaded Successful')
        return super(FormPageView, self).form_valid(form)
