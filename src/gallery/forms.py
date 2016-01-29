from django import forms


class GalleryForm(forms.Form):
    image = forms.FileField(
        label='Select an image'
    )
    
