from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import AssetForm

# Create your views here.
def index(request):
    #とりあえず文字列を返す。
    return render(request, 'index.html')

class AssetCreateView(CreateView):
    template_name = 'create.html'
    form_class = AssetForm
    success_url = reverse_lazy('asset:create')

class AssetCreateCompleteView(TemplateView):
    template_name = 'complete.html'