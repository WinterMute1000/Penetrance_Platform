# from django.shortcuts import render
from django.views.generic import CreateView
# from django.views.generic.edit import FormMixin
from django.template import loader
from django.http import HttpResponse, JsonResponse
from .forms import HashGeneratorForm
from .hash_generator_module.hash_generator_class import HashGeneratorClass


# Create your views here.

class HashGeneratorView(CreateView):
    form_class = HashGeneratorForm
    # key = hash algorithm, value =encrypt
    hash_function_dict = {'MD5': HashGeneratorClass.md5_encrypt,
                          'SHA1': HashGeneratorClass.sha1_encrypt,
                          'SHA256': HashGeneratorClass.sha256_encrypt,
                          'SHA512': HashGeneratorClass.sha512_encrypt}

    def get(self, request, *args, **kwargs):
        context = {'form': HashGeneratorForm()}

        hash_generator_template = loader.get_template('hash_generator.html')
        return HttpResponse(hash_generator_template.render(context, request))

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            target_str = form.data['target_str']
            hash_choice = str(form.data['hash_choice'])

            result = self.hash_function_dict[hash_choice](target_str)

            return JsonResponse({'result': result}, json_dumps_params={'ensure_ascii': True})

        return JsonResponse({'result': "String Error or Not Choice Encode or Decode"},
                            json_dumps_params={'ensure_ascii': True})
