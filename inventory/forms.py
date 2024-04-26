from django import forms
from product.models import car_model, Accessary

class add_car_product_forms(forms.ModelForm):
    
    car_name = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.TextInput(attrs={
            'type': "text",
            'class': "form--element",
            'name': "car_name",
            'placeholder': "Name",
        })
    )
    
    car_company = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': "form--element",
            'placeholder': "Company",
        })
    )
    
    car_price = forms.CharField(
        required=True,
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': "form--element",
            'placeholder': "Price",
        })
    )
    
    car_color = forms.ChoiceField(
        choices=car_model.car_color_choice, 
        widget=forms.Select(
            attrs={
                'class': 'form-control'
                }
            )
        )
    
    car_information = forms.CharField(
        required=True,
        max_length=200,
        widget=forms.Textarea(attrs={
            'class': "form--element",
            'placeholder': "Description",
        })
    )
    
    car_year = forms.CharField(
        required=True,
        max_length=5,
        widget=forms.TextInput(attrs={
            'class': "form--element",
            'placeholder': "Year",
        })
    )
    
    car_images = forms.FileField(
        required=True,
        widget=forms.FileInput(attrs={
            'name': "car_images" ,
            'class': "custom-file-input",
            'onchange': "previewImage(this)",
        })
    )
    
    class Meta:
        model = car_model
        fields = ["car_name", "car_company", "car_price", "car_color", "car_information", "car_images", "car_year"]
        
class add_accessary_product_forms(forms.ModelForm):
    
    accessary_name = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.TextInput(attrs={
            'type': "text",
            'class': "form--element",
            'name': "car_name",
            'placeholder': "Name",
        })
    )
    
    accessary_company = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': "form--element",
            'placeholder': "Company",
        })
    )
    
    accessary_price = forms.CharField(
        required=True,
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': "form--element",
            'placeholder': "Price",
        })
    )
    
    accessary_info = forms.CharField(
        required=True,
        max_length=200,
        widget=forms.Textarea(attrs={
            'class': "form--element",
            'placeholder': "Description",
        })
    )
    
    accessary_images = forms.FileField(
        required=True,
        widget=forms.FileInput(attrs={
            'name': "car_images" ,
            'class': "custom-file-input",
            'onchange': "previewImage(this)",
        })
    )
    
    class Meta:
        model = Accessary
        fields = ["accessary_name", "accessary_company", "accessary_price", "accessary_info", "accessary_images"]