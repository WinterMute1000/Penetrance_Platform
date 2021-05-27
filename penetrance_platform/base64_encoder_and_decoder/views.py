# from django.shortcuts import render
from django.views.generic import CreateView
# from django.views.generic.edit import FormMixin
from django.template import loader
from django.http import HttpResponse, JsonResponse
from .forms import Base64EncoderAndDecoderForm
import base64


# Create your views here.

class Base64EncoderAndDecoderView(CreateView):
    form_class = Base64EncoderAndDecoderForm

    def get(self, request, *args, **kwargs):
        context = {'form': Base64EncoderAndDecoderForm()}

        base64_encoder_and_decoder_template = loader.get_template('base64_encoder_and_decoder.html')
        return HttpResponse(base64_encoder_and_decoder_template.render(context, request))

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            target_str = form.data['target_str']
            encode_or_decode = form.data['encode_or_decode']

            # Base64 Encode
            if encode_or_decode == 'Encode':
                result = str(base64.b64encode(target_str.encode('utf-8'))).replace('b', '').replace('\'', ' ')
            # Base64 Decode
            elif encode_or_decode == 'Decode':
                result = str(base64.b64decode(target_str.encode('utf-8'))).replace('b', '').replace('\'', ' ')
            # Who can approach this state?
            else:
                result = "How can you doing?"

            return JsonResponse({'result': result}, json_dumps_params={'ensure_ascii': True})

        return JsonResponse({'result': "String Error or Not Choice Encode or Decode"},
                            json_dumps_params={'ensure_ascii': True})
