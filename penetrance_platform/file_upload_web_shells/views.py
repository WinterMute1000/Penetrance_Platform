from django.shortcuts import render
from django.views.generic import ListView
from .models import FileUploadWebShells
from django.template import loader
from django.http import HttpResponse


# Create your views here.

class FileUploadWebShellsView(ListView):
    def get(self, request, *args, **kwargs):
        context = {'web_shells': FileUploadWebShells.objects.all()}

        file_upload_web_shells_template = loader.get_template('file_upload_web_shells.html')
        return HttpResponse(file_upload_web_shells_template.render(context, request))
