from django import forms


class Base64EncoderAndDecoderForm(forms.Form):
    ENCODE_RADIO_BUTTON = [('Encode', 'Encode'), ('Decode', 'Decode')]
    target_str = forms.CharField(widget=forms.TextInput(attrs={'size': '50', 'class': 'inputText'}))
    encode_or_decode = forms.ChoiceField(required=True, choices=ENCODE_RADIO_BUTTON, widget=forms.RadioSelect)

    def is_valid(self):
        target_str = self.data['target_str']
        encode_or_decode = self.data['encode_or_decode']

        if target_str is None:
            return False

        if encode_or_decode is None:
            return False

        return True
