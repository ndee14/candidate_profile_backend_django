# core/views.py
from django.views.generic import TemplateView

class UploadView(TemplateView):
    template_name = 'upload.html'


class ProfileView(TemplateView):
    template_name = 'profile.html'