from django import forms
from catalog.models import Product, Version

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    exceptions_list = ['казино',
                       'криптовалюта',
                       'крипта',
                       'биржа',
                       'дешево',
                       'бесплатно',
                       'обман',
                       'полиция',
                       'радар']

    def clean_title(self):
        cleaned_data = self.cleaned_data['title']

        for word in ProductForm.exceptions_list:
            if word in cleaned_data:
                raise forms.ValidationError(f'В названии и описании не должно содеражться слов: {", ".join(ProductForm.exceptions_list)}.')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        for word in ProductForm.exceptions_list:
            if word in cleaned_data:
                raise forms.ValidationError(
                    f'В названии и описании не должно содеражться слов: {",".join(ProductForm.exceptions_list)}.')

        return cleaned_data


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
