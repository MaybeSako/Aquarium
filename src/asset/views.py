from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, DetailView, UpdateView
from django.utils import timezone

from .forms import AssetForm
from .models import Asset

# Create your views here.
def index(request):
    #とりあえず文字列を返す。
    return render(request, 'asset_index.html') ##最終的には、sample配下のindex.htmlに変更を検討する

class AssetCreateView(CreateView):
    template_name = 'create.html'
    form_class = AssetForm
    success_url = reverse_lazy('asset:asset_create')

class AssetCreateCompleteView(TemplateView):
    template_name = 'complete.html'

class AssetListView(ListView):
    template_name = 'asset_list.html'
    model = Asset

class AssetDetailView(DetailView):
    template_name = 'asset_detail.html'
    model = Asset

class AssetUpdateView(UpdateView):
    template_name = 'asset_update.html'
    model = Asset
    fields = ('name', 'price', 'text',)
    success_url = reverse_lazy('asset:asset_list')

    def form_valid(self, form):
        asset = form.save(commit=False)
        asset.updated_at = timezone.now()
        asset.save()
        return super().form_valid(form)