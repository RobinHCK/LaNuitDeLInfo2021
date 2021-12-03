from django import forms
from .models import Image

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


class ImageForm(forms.ModelForm):
    """Form for the image model"""

    class Meta:
        model = Image
        fields = ('img')