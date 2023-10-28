from django import forms
from django.forms import Select, TextInput, Textarea

from product.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'category': Select(attrs={'class': 'form-select'}),
            'title': TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Please enter the product title'}),
            'author': TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Please enter the author'}),
            'description': Textarea(attrs={'class': 'form-control',
                                           'placeholder': 'Please enter the product description'}),
            'price': forms.TextInput(
                attrs={'type': 'number', 'step': '0.01', 'min': '0.01',
                       'class': 'form-control'}),
            'in_stock': forms.CheckboxInput(
                attrs={'class': 'form-check-input'}),
            'is_active': forms.CheckboxInput(
                attrs={'class': 'form-check-input'}),
            'recommended_age': forms.TextInput(attrs={'class': 'form-control',
                                                      'placeholder': 'Please enter the product recommended age'}),
            'language': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Please enter the product language'}),
            'publication_date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}),
            'publisher': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Please enter the product publisher'}),
            'cover_type': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Please enter the cover type'}),
            'page_count': forms.NumberInput(attrs={'class': 'form-control',
                                                   'placeholder': 'Please enter the product page count'}),
            'isbn': forms.NumberInput(attrs={'class': 'form-control',
                                             'placeholder': 'Please enter the product isbn'}),
            'dimensions_length': forms.NumberInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Please enter the product dimensions length'}),
            'dimensions_height': forms.NumberInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Please enter the product dimensions height'}),
        }


    def clean(self):
        cleaned_data = self.cleaned_data

        get_description = cleaned_data['description']
        if len(get_description) < 20:
            msg = 'You must add at least 20 characters!'
            self._errors['description'] = self.error_class([msg])


        get_isbn = cleaned_data.get('isbn', '')  # Obține ISBN-ul, sau un șir gol dacă nu există
        if get_isbn and len(str(get_isbn)) > 13:
            msg = 'ISBN cannot exceed 13 characters!'
            self._errors['isbn'] = self.error_class([msg])
        elif get_isbn and len(str(get_isbn)) < 10:
            msg = 'ISBN must contain at least 10 characters!'
            self._errors['isbn'] = self.error_class([msg])

        return cleaned_data






class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'category': Select(attrs={'class': 'form-select'}),
            'title': TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Please enter the product title'}),
            'author': TextInput(attrs={'class': 'form-control',
                                       'placeholder': 'Please enter the author'}),
            'description': Textarea(attrs={'class': 'form-control',
                                           'placeholder': 'Please enter the product description'}),
            'price': forms.TextInput(
                attrs={'type': 'number', 'step': '0.01', 'min': '0.01',
                       'class': 'form-control'}),
            'in_stock': forms.CheckboxInput(
                attrs={'class': 'form-check-input'}),
            'is_active': forms.CheckboxInput(
                attrs={'class': 'form-check-input'}),
            'recommended_age': forms.TextInput(attrs={'class': 'form-control',
                                                      'placeholder': 'Please enter the product recommended age'}),
            'language': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Please enter the product language'}),
            'publication_date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}),
            'publisher': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Please enter the product publisher'}),
            'cover_type': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Please enter the cover type'}),
            'page_count': forms.NumberInput(attrs={'class': 'form-control',
                                                   'placeholder': 'Please enter the product page count'}),
            'isbn': forms.NumberInput(attrs={'class': 'form-control',
                                             'placeholder': 'Please enter the product isbn'}),
            'dimensions_length': forms.NumberInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Please enter the product dimensions length'}),
            'dimensions_height': forms.NumberInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Please enter the product dimensions height'}),
        }