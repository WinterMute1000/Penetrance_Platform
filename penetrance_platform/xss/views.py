from django.shortcuts import render
# from django.shortcuts import render
from django.views.generic import CreateView
# from django.views.generic.edit import FormMixin
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.core.signals import request_finished
from django.dispatch
from .forms import XSSForm
from .models import XSSLog
from .xss_module.xss_module import XSSModule


# Create your views here.

class XSSView(CreateView):
    form_class = XSSForm

    def get(self, request, *args, **kwargs):
        context = {'form': XSSForm()}

        information_disclosure_template = loader.get_template('information_disclosure.html')
        return HttpResponse(information_disclosure_template.render(context, request))

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
