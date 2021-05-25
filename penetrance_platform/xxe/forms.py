from django import forms


class XXEForm(forms.Form):
    METHOD_RADIO_BUTTON = [('GET', 'GET'), ('POST', 'POST')]
    host = forms.CharField(required=True, help_text="Input host address or domain name")
    param_name = forms.CharField(required=True, help_text="Input name parameter")
    method = forms.ChoiceField(required=True, choices=METHOD_RADIO_BUTTON, widget=forms.RadioSelect)
    logging = forms.BooleanField(initial=False, required=False, help_text="Check if you want logging.",
                                 widget=forms.CheckboxInput())

    def is_valid(self):
        host = self.data['host']
        param_name = self.data['param_name']
        method = self.data['method']

        if len(host) > 2048 or host is None:
            return False

        if param_name is None:
            return False
        if method is None:
            return False

        return True
