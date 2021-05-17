from django import forms


class InformationDisclosureForm(forms.Form):
    host = forms.CharField(required=True, help_text="Input host address or domain name")
    logging = forms.BooleanField(initial=False, required=False, help_text="Check if you want logging.",
                                 widget=forms.CheckboxInput())

    def is_valid(self):
        host = self.data['host']

        if len(host) > 2048 or host is None:
            return False

        return True
