from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.edit import FormMixin
from django.template import loader
from django.http import HttpResponse, JsonResponse
from .forms import InformationDisclosureForm
from .models import InformationDisclosureLog


# Create your views here.

class InformationDisclosureView(CreateView):
    form_class = InformationDisclosureForm

    def get(self, request, *args, **kwargs):
        context = {'form': InformationDisclosureForm()}

        information_disclosure_template = loader.get_template('information_disclosure.html')
        return HttpResponse(information_disclosure_template.render(context, request))
