# core/views.py
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'template/upload.html'