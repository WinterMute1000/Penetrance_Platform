from django import forms


class HashGeneratorForm(forms.Form):
    VALID_RADIO_BUTTON_VALUES = ['Encrypt', 'Decrypt']
    VALID_HASH_CHOICE_VALUES= ['MD5', 'SHA1', 'SHA256', 'SHA512']
    HASH_CHOICE_FILED = [('MD5', 'MD5'), ('SHA1', 'SHA1'), ('SHA256', 'SHA256'),
                         ('SHA512', 'SHA512')]
    ENCRYPT_OR_DECRYPT_CHOICE_RADIO_BUTTON = [('Encrypt', 'Encrypt'), ('Decrypt', 'Decrypt')]
    target_str = forms.CharField(widget=forms.TextInput(attrs={'size': '50', 'class': 'inputText'}))
    hash_choice = forms.ChoiceField(required=True, choices=HASH_CHOICE_FILED)
    encrypt_or_decrypt = forms.ChoiceField(required=True,
                                           choices=ENCRYPT_OR_DECRYPT_CHOICE_RADIO_BUTTON, widget=forms.RadioSelect)

    def is_valid(self):
        target_str = self.data['target_str']
        hash_choice = self.data['hash_choice']
        encrypt_or_decrypt = self.data['encrypt_or_decrypt']

        if target_str is None:
            return False
        if hash_choice is None or hash_choice not in self.VALID_HASH_CHOICE_VALUES:
            return False
        if encrypt_or_decrypt is None or encrypt_or_decrypt not in self.VALID_RADIO_BUTTON_VALUES:
            return False

        return True
